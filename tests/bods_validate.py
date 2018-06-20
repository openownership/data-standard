import os
import json
from collections import OrderedDict
from jsonschema import validate, RefResolver, FormatChecker
from jsonschema.validators import Draft4Validator
from jsonschema.exceptions import ValidationError


this_dir = os.path.dirname(os.path.realpath(__file__))
absolute_path_to_schema_dir = this_dir + '/../schema/'
resolver = RefResolver('file://' + absolute_path_to_schema_dir + '/', None)
format_checker = FormatChecker()


class MissingStatementTypeError(ValidationError):
    pass


class UnknownStatementTypeError(ValidationError):
    pass


class UnrecognisedStatementID(ValidationError):
    pass


def schema_path_from_statement(statement):
    schemas = {
        'entityStatement': 'entity-statement.json',
        'personStatement': 'person-statement.json',
        'beneficialOwnershipStatement': 'beneficial-ownership-statement.json',
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
    if statement_type == 'beneficialOwnershipStatement':
        entity_statement_id = statement.get('subject', {}).get('entity', {}).get('describedByStatement')
        if entity_statement_id not in entity_statement_ids:
            raise UnrecognisedStatementID("subject/entity/describedByStatement '{}' does not match any known entities".format(entity_statement_id))
        if 'person' in statement.get('interestedParty', {}):
            person_statement_id = statement.get('interestedParty', {}).get('person', {}).get('describedByStatement')
            if person_statement_id not in person_statement_ids:
                raise UnrecognisedStatementID("interestedParty/person/describedByStatement '{}' does not match any known persons".format(person_statement_id))
        if 'entity' in statement.get('interestedParty', {}):
            interested_entity_statement_id = statement.get('interestedParty', {}).get('entity', {}).get('describedByStatement')
            if interested_entity_statement_id not in entity_statement_ids:
                raise UnrecognisedStatementID("interestedParty/entity/describedByStatement '{}' does not match any known entities".format(interested_entity_statement_id))


def bods_validate_statement(statement):
    schema_path = schema_path_from_statement(statement)
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f, object_pairs_hook=OrderedDict)
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
