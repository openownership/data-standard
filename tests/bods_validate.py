import os
import json
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


def bods_validate_statement(statement):
    schema_path = schema_path_from_statement(statement)
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f)
    validate(statement, schema, resolver=resolver, format_checker=format_checker)


def bods_validate_package(statement_list):
    for statement in statement_list:
        bods_validate_statement(statement)


def bods_iter_errors_statement(statement):
    try:
        schema_path = schema_path_from_statement(statement)
    except (MissingStatementTypeError, UnknownStatementTypeError) as e:
        yield e
        return
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f)
    validator = Draft4Validator(schema, resolver=resolver, format_checker=format_checker)
    yield from validator.iter_errors(statement)


def bods_iter_errors_package(statement_list):
    for statement in statement_list:
        yield from bods_iter_errors_statement(statement)
