import os
import json
import pytest
from jsonschema import validate, ValidationError

from bods_validate import this_dir, format_checker, absolute_path_to_schema_dir, resolver
from bods_validate import MissingStatementTypeError, UnrecognisedStatementID
from bods_validate import bods_validate_package, bods_validate_statement
from bods_validate import bods_iter_errors_package, bods_iter_errors_statement


@pytest.mark.parametrize('json_path', [
    'data/entity-statement/valid/valid-entity-statement.json',
    'data/person-statement/valid/valid-person-statement.json',
    'data/beneficial-ownership-statement/valid/valid-beneficial-ownership-statement.json',
    '../examples/flat-serialisation/gb-coh-entity-statement.json',
    '../examples/flat-serialisation/gb-coh-person-statement.json',
])
def test_valid_statement_json(json_path):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f)
    bods_validate_statement(json_data)


@pytest.mark.parametrize('json_path', [
    'data/bods-package/valid/valid-bods-package.json',
    'data/bods-package/valid/valid-bods-package-entity-owning-entity.json',
    '../examples/flat-serialisation/gb-coh-bods-package.json',
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
    ('data/entity-statement/invalid/entity-statement-with-invalid-statement-id-no-entity-type.json', ValidationError),
    ('data/person-statement/invalid/person-statement-with-invalid-statement-id.json', ValidationError),
    ('data/person-statement/invalid/person-statement-with-bad-date.json', ValidationError),
    ('data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-with-invalid-statement-id.json', ValidationError),
    ('data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-no-statement-type.json', MissingStatementTypeError),
])
def test_invalid_statement_json(json_path, error):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f)
    with pytest.raises(error):
        bods_validate_statement(json_data)


@pytest.mark.parametrize(('json_path', 'json_paths', 'error'), [
    (None, [
        'data/entity-statement/valid/valid-entity-statement.json',
        'data/person-statement/valid/valid-person-statement.json',
        'data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-with-invalid-statement-id.json',
    ], ValidationError),
    (None, [
        'data/entity-statement/valid/valid-entity-statement.json',
        'data/person-statement/valid/valid-person-statement.json',
        'data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-no-statement-type.json',
    ], MissingStatementTypeError),
    ('data/bods-package/fails-secondary-validation/bods-package-missing-entity-statement.json', None, UnrecognisedStatementID),
])
def test_invalid_package_json(json_path, json_paths, error):
    if json_path:
        with open(os.path.join(this_dir, json_path)) as f:
            json_data = json.load(f)
    else:
        json_data = [json.load(open(os.path.join(this_dir, json_path))) for json_path in json_paths]

    # Validate statement by statement
    with pytest.raises(error):
        bods_validate_package(json_data)

    # We don't get unrecognised statement errors if we validate the whole
    # package
    if error is UnrecognisedStatementID:
        return

    # Validate the whole package at once
    schema_path = 'bods-package.json'
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f)
    with pytest.raises(ValidationError):
        validate(json_data, schema, resolver=resolver, format_checker=format_checker)


@pytest.mark.parametrize(('json_path', 'expected_errors'), [
    ('data/entity-statement/valid/valid-entity-statement.json', set()),
    ('data/person-statement/valid/valid-person-statement.json', set()),
    ('data/beneficial-ownership-statement/valid/valid-beneficial-ownership-statement.json', set()),
    ('data/entity-statement/invalid/entity-statement-with-invalid-statement-id.json', {
        "'too-short-so-fail' is too short"
    }),
    ('data/entity-statement/invalid/entity-statement-with-invalid-statement-id-no-entity-type.json', {
        "'too-short-so-fail' is too short",
        "'entityType' is a required property",
    }),
    ('data/person-statement/invalid/person-statement-with-invalid-statement-id.json', {
        "'too-short-so-fail' is too short"
    }),
    ('data/person-statement/invalid/person-statement-with-bad-date.json', {
        "'Tuesday' is not a 'date'",
    }),
    ('data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-with-invalid-statement-id.json', {
        "'too-short-so-fail' is too short",
    }),
    ('data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-no-statement-type.json', {
        "'statementType' is a required property",
    }),
])
def test_invalid_statement_json_iter_errors(json_path, expected_errors):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f)
    actual_errors = {e.message for e in bods_iter_errors_statement(json_data)}
    assert actual_errors == expected_errors


@pytest.mark.parametrize(('json_path', 'json_paths', 'expected_errors'), [
    ('data/bods-package/valid/valid-bods-package.json', None, set()),
    (None, [
        'data/entity-statement/valid/valid-entity-statement.json',
        'data/person-statement/valid/valid-person-statement.json',
        'data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-with-invalid-statement-id.json',
    ], {
        "'too-short-so-fail' is too short"
    }),
    (None, [
        'data/entity-statement/valid/valid-entity-statement.json',
        'data/person-statement/valid/valid-person-statement.json',
        'data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-no-statement-type.json',
    ], {
        "'statementType' is a required property",
    }),
    ('data/bods-package/fails-secondary-validation/bods-package-missing-entity-statement.json', None, {
        "subject/entitiy/describedByStatement '1dc0e987-5c57-4a1c-b3ad-61353b66a9b7' does not match any known entities"
    }),
])
def test_invalid_package_json_iter_errors(json_path, json_paths, expected_errors):
    if json_path:
        with open(os.path.join(this_dir, json_path)) as f:
            json_data = json.load(f)
    else:
        json_data = [json.load(open(os.path.join(this_dir, json_path))) for json_path in json_paths]
    actual_errors = {e.message for e in bods_iter_errors_package(json_data)}
    assert actual_errors == expected_errors
