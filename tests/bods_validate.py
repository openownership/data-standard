import os
import json
from jsonschema import validate, RefResolver, FormatChecker


this_dir = os.path.dirname(os.path.realpath(__file__))
absolute_path_to_schema_dir = this_dir + '/../schema/'
resolver = RefResolver('file://' + absolute_path_to_schema_dir + '/', None)
format_checker = FormatChecker()


class MissingStatementTypeError(ValueError):
    pass


class UnknownStatementTypeError(ValueError):
    pass


def bods_validate_statement(statement):
    schemas = {
        'entityStatement': 'entity-statement.json',
        'personStatement': 'person-statement.json',
        'beneficialOwnershipStatement': 'beneficial-ownership-statement.json',
    }
    statement_type = statement.get('statementType')
    if not statement_type:
        raise MissingStatementTypeError()
    schema_path = schemas.get(statement_type)
    if not schema_path:
        raise UnknownStatementTypeError('Unknown statementType {}'.format(statement.get('statementType')))
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f)
    validate(statement, schema, resolver=resolver, format_checker=format_checker)


def bods_validate_package(statement_list):
    for statement in statement_list:
        bods_validate_statement(statement)
