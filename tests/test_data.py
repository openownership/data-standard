import os
import json
import pytest
from jsonschema import validate, ValidationError

from bods_validate import this_dir, format_checker, absolute_path_to_schema_dir, resolver
from bods_validate import MissingStatementTypeError
from bods_validate import bods_validate_package, bods_validate_statement


@pytest.mark.parametrize('json_path', [
    'data/entity-statement/valid/valid-entity-statement.json',
    'data/person-statement/valid/valid-person-statement.json',
    'data/beneficial-ownership-statement/valid/valid-beneficial-ownership-statement.json',
    pytest.mark.xfail('../examples/flat-serialisation/gb-coh-entity-statement.json'),
    '../examples/flat-serialisation/gb-coh-person-statement.json',
])
def test_valid_statement_json(json_path):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f)
    bods_validate_statement(json_data)


@pytest.mark.parametrize('json_path', [
    'data/bods-package/valid/valid-bods-package.json',
    '../examples/flat-serialisation/gb-coh-bods-package.json',
    pytest.mark.xfail('../examples/flat-serialisation/single-direct.json'),
])
def test_valid_package_json(json_path):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f)
    assert isinstance(json_data, list)

    # Validate statement by statement
    bods_validate_package(json_data)

    # Validate the whole package at once
    schema_path = 'bods-package.json'
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f)
    validate(json_data, schema, resolver=resolver, format_checker=format_checker)


@pytest.mark.parametrize(('json_path', 'error'), [
    ('data/entity-statement/invalid/entity-statement-with-invalid-statement-id.json', ValidationError),
    ('data/person-statement/invalid/person-statement-with-invalid-statement-id.json', ValidationError),
    ('data/person-statement/invalid/person-statement-with-bad-date.json', ValidationError),
    ('data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-with-invalid-statement-id.json', ValidationError),
    ('data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-no-statement-type.json', MissingStatementTypeError),
])
def test_invalid_json(json_path, error):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f)
    with pytest.raises(error):
        bods_validate_statement(json_data)


@pytest.mark.parametrize(('json_paths', 'error'), [
    ([
        'data/entity-statement/valid/valid-entity-statement.json',
        'data/person-statement/valid/valid-person-statement.json',
        'data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-with-invalid-statement-id.json',
    ], ValidationError),
    ([
        'data/entity-statement/valid/valid-entity-statement.json',
        'data/person-statement/valid/valid-person-statement.json',
        'data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-no-statement-type.json',
    ], MissingStatementTypeError),
])
def test_invalid_package(json_paths, error):
    json_data = [json.load(open(os.path.join(this_dir, json_path))) for json_path in json_paths]
    schema_path = 'bods-package.json'
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f)

    # Validate statement by statement
    with pytest.raises(error):
        bods_validate_package(json_data)

    # Validate the whole package at once
    schema_path = 'bods-package.json'
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f)
    with pytest.raises(ValidationError):
        validate(json_data, schema, resolver=resolver, format_checker=format_checker)
