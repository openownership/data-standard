import os
import json
import pytest

from pathlib import Path
from jsonschema import FormatChecker
from jsonschema.validators import Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

def get_json_files(dir):
    """
    Recursively gets files with .json extension in `path` and returns
    a list of the full paths.
    """
    paths = []
    for p in Path(dir).rglob('*.json'):
        paths.append(p)
    return paths

def file_id(path):
    return path.name

@pytest.fixture
def bods_validator():
    """
    This loads the five BODS schema files into a jsonschema registry, so the validator can resolve $refs across all of the schema files.

    Then sets up and returns the validator, using the statement.json
    schema as the primary schema against which data is validated.
    """

    # Get schema JSON files from disc
    here = os.path.dirname(os.path.realpath(__file__))
    schema_paths = [
        ("urn:statement", here + "/../schema/statement.json"),
        ("urn:person", here + "/../schema/person-record.json"),
        ("urn:entity", here + "/../schema/entity-record.json"),
        ("urn:relationship", here + "/../schema/relationship-record.json"),
        ("urn:components", here + "/../schema/components.json")
    ]

    # Load schemas into in-memory registry
    # View contents with eg. print(registry.contents("urn:statement"))
    schemas = []
    for schema_id, schema_path in schema_paths:
        with open(schema_path) as f:
            schemas.append((schema_id, Resource(contents=json.load(f), specification=DRAFT202012)))

    registry = Registry().with_resources(schemas)

    # Get meta schema
    with open(os.path.join(here, 'schema', 'meta-schema.json')) as fp:
        metaschema = json.load(fp)

    validator = Draft202012Validator(metaschema, registry=registry, format_checker=FormatChecker())

    statement_schema = registry.contents("urn:statement")
    bods_validator = validator.evolve(schema=statement_schema)
    return bods_validator

@pytest.fixture
def bods_json(request):
    p = Path(request.param)
    bods = json.loads(p.read_text())
    return bods

@pytest.fixture
def get_valid_data():
    """
    Returns a simple valid BODS statement.
    """
    data = {
        "statementId": "abcdefgkdddddddddddddddddddddddshdkjfkjdkjf",
        "declarationSubject": "xyz",
        "recordId": "123",
        "recordType": "entity",
        "recordDetails": {
            "entityType": "unknownEntity",
            "isComponent": False,
            "publicationDetails": {}
        }
    }
    return data

@pytest.fixture
def get_invalid_data():
    """
    Returns a simple invalid BODS statement.
    """
    data = {
        "declarationSubject": "xyz",
        "recordId": "123",
        "recordType": "entity"
    }
    return data


valid_bods_files = get_json_files(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "v0.4", "valid"))

@pytest.mark.parametrize("bods_json", valid_bods_files, ids=file_id, indirect=True)
def test_valid_files(bods_validator, bods_json):
    is_valid = bods_validator.is_valid(bods_json)
    assert is_valid == True

def test_valid_data(bods_validator, get_valid_data):
    is_valid = bods_validator.is_valid(get_valid_data)
    assert is_valid == True

def test_invalid_data(bods_validator, get_invalid_data):
    is_valid = bods_validator.is_valid(get_valid_data)
    assert is_valid == False

# errors = bods_validator.iter_errors(data)

# for error in errors:
#     print(error.message)