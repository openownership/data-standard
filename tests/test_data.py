import os
import json
from jsonschema import validate, ValidationError, RefResolver
import pytest


this_dir = os.path.dirname(os.path.realpath(__file__))
absolute_path_to_schema_dir = this_dir  + '/../schema/'
resolver = RefResolver('file://' + absolute_path_to_schema_dir + '/', None)


@pytest.mark.parametrize(('json_path', 'schema_path'), [
    ('data/entity-statement/valid/valid-entity-statement.json', 'entity-statement.json'),
    ('data/person-statement/valid/valid-person-statement.json', 'person-statement.json'),
    ('data/beneficial-ownership-statement/valid/valid-beneficial-ownership-statement.json', 'beneficial-ownership-statement.json'),
    ('data/bods-package/valid/valid-bods-package.json', 'bods-package.json'),
])
def test_valid_json(json_path, schema_path):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f)
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f)
    validate(json_data, schema, resolver=resolver)


@pytest.mark.parametrize(('json_path', 'schema_path'), [
    ('data/entity-statement/invalid/entity-statement-with-invalid-statement-id.json', 'entity-statement.json'),
    ('data/person-statement/invalid/person-statement-with-invalid-statement-id.json', 'person-statement.json'),
    ('data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-with-invalid-statement-id.json', 'beneficial-ownership-statement.json'),
    ('data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-no-statement-type.json', 'beneficial-ownership-statement.json'),
])
def test_invalid_json(json_path, schema_path):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f)
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f)
    with pytest.raises(ValidationError):
        validate(json_data, schema, resolver=resolver)


@pytest.mark.parametrize('json_paths', [
    [
        'data/entity-statement/valid/valid-entity-statement.json',
        'data/person-statement/valid/valid-person-statement.json',
        'data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-with-invalid-statement-id.json',
    ],
    [
        'data/entity-statement/valid/valid-entity-statement.json',
        'data/person-statement/valid/valid-person-statement.json',
        'data/beneficial-ownership-statement/invalid/beneficial-ownership-statement-no-statement-type.json',
    ],
])
def test_invalid_package(json_paths):
    json_data = [json.load(open(os.path.join(this_dir, json_path))) for json_path in json_paths]
    schema_path = 'bods-package.json'
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f)
    with pytest.raises(ValidationError):
        validate(json_data, schema, resolver=resolver)

