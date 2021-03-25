import os
import json
from collections import OrderedDict
from jsonschema import validate, RefResolver, FormatChecker
from jsonschema.validators import Draft4Validator
from jsonschema.exceptions import ValidationError
from compiletojsonschema.compiletojsonschema import CompileToJsonSchema


this_dir = os.path.dirname(os.path.realpath(__file__))
absolute_path_to_source_schema_dir = this_dir + '/../schema/'
absolute_path_to_schema_dir = this_dir + '/../schema/testing/'
resolver = RefResolver('file://' + absolute_path_to_schema_dir + '/', None)
format_checker = FormatChecker()


class MissingStatementTypeError(ValidationError):
    pass


class UnknownStatementTypeError(ValidationError):
    pass


class UnrecognisedStatementID(ValidationError):
    pass


def build_schemas_for_testing():
    os.makedirs(absolute_path_to_schema_dir, exist_ok=True)
    source_files = [f for f in os.listdir(absolute_path_to_source_schema_dir)
                    if os.path.isfile(os.path.join(absolute_path_to_source_schema_dir, f))]
    for source_file in source_files:
        if source_file.endswith('.json'):
            ctjs = CompileToJsonSchema(
                os.path.join(absolute_path_to_source_schema_dir, source_file),
                set_additional_properties_false_everywhere=True,
                codelist_base_directory=absolute_path_to_source_schema_dir + '/codelists/'
            )
            with open(os.path.join(absolute_path_to_schema_dir, source_file), "w") as fp:
                created_json = json.loads(ctjs.get_as_string())
                # write with correct indentation
                fp.write(json.dumps(created_json, ensure_ascii=False, indent=2, separators=(',', ': ')) + '\n')


def schema_path_from_statement(statement):
    schemas = {
        'annotationStatement': 'annotation-statement.json',
        'entityStatement': 'entity-statement.json',
        'personStatement': 'person-statement.json',
        'ownershipOrControlStatement': 'ownership-or-control-statement.json',
    }
    statement_type = statement.get('statementType')
    if not statement_type:
        raise MissingStatementTypeError("'statementType' is a required property")
    schema_path = schemas.get(statement_type)
    if not schema_path:
        raise UnknownStatementTypeError('Unknown statementType {}'.format(statement.get('statementType')))
    return schema_path


def check_ids(statement, entity_statement_ids, person_statement_ids):
    statement_type = statement.get('statementType')
    statement_id = statement.get('statementID')
    if statement_id:
        if statement_type == 'entityStatement':
            entity_statement_ids.add(statement_id)
        elif statement_type == 'personStatement':
            person_statement_ids.add(statement_id)
    if statement_type == 'ownershipOrControlStatement':
        entity_statement_id = statement.get('subject', {}).get('describedByEntityStatement', '')
        if entity_statement_id not in entity_statement_ids:
            raise UnrecognisedStatementID("subject/describedByEntityStatement '{}' does not match any known entities".format(entity_statement_id))
        if 'describedByPersonStatement' in statement.get('interestedParty', {}):
            person_statement_id = statement.get('interestedParty', {}).get('describedByPersonStatement')
            if person_statement_id not in person_statement_ids:
                raise UnrecognisedStatementID("interestedParty/describedByPersonStatement '{}' does not match any known persons".format(person_statement_id))
        if 'describedByEntityStatement' in statement.get('interestedParty', {}):
            interested_entity_statement_id = statement.get('interestedParty', {}).get('describedByEntityStatement')
            if interested_entity_statement_id not in entity_statement_ids:
                raise UnrecognisedStatementID("interestedParty/describedByEntityStatement '{}' does not match any known entities".format(interested_entity_statement_id))


def bods_validate_statement(statement):
    schema_path = schema_path_from_statement(statement)
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f, object_pairs_hook=OrderedDict)
    schema['additionalProperties'] = False
    validate(statement, schema, resolver=resolver, format_checker=format_checker)


def bods_validate_package(statement_list):
    entity_statement_ids = set()
    person_statement_ids = set()
    for statement in statement_list:
        check_ids(statement, entity_statement_ids, person_statement_ids)
        bods_validate_statement(statement)


def bods_iter_errors_statement(statement):
    """
    Returns an iterable of `ValidationError`'s for a BODS statement.
    https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError

    """
    try:
        schema_path = schema_path_from_statement(statement)
    except (MissingStatementTypeError, UnknownStatementTypeError) as e:
        yield e
        return
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f, object_pairs_hook=OrderedDict)
    validator = Draft4Validator(schema, resolver=resolver, format_checker=format_checker)
    yield from validator.iter_errors(statement)


def bods_iter_errors_package(statement_list):
    """
    Returns an iterable of `ValidationError`'s for a BODS package.
    https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError

    """
    entity_statement_ids = set()
    person_statement_ids = set()
    for statement in statement_list:
        try:
            check_ids(statement, entity_statement_ids, person_statement_ids)
        except UnrecognisedStatementID as e:
            yield e
        yield from bods_iter_errors_statement(statement)
