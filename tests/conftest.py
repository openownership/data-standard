import os
import json
import pytest

from pathlib import Path
from jsonschema import FormatChecker
from jsonschema.validators import Draft202012Validator
from jscc.schema import is_json_schema
from jscc.testing.filesystem import walk_json_data
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


def schema_paths():
    here = os.path.dirname(os.path.realpath(__file__))
    schema_dir = os.path.join(here, "..", "schema")
    schema_paths = [(path, name, data) for path, name, _, data in walk_json_data(top=schema_dir) if is_json_schema(data)]
    return schema_paths


def schema_registry():
    """
    This loads the BODS schema files into a jsonschema registry, so the
    validator can resolve $refs across all of the schema files.
    """
    schemas = []
    for path, name, schema in schema_paths():
        schemas.append((schema.get('$id'), Resource(contents=schema, specification=DRAFT202012)))

    registry = Registry().with_resources(schemas)
    return registry


"""
The fixtures in this file are automatically discovered by pytest without
needing to import them in the test files.
"""


@pytest.fixture
def schema_from_registry(request):
    registry = schema_registry()
    return registry.contents(request.param)


@pytest.fixture
def schema_validator():
    """
    This sets up and returns a 2020-12 validator, against which the BODS
    schema can be checked. The BODS schema files are loaded into the
    registry so $refs can be resolved.
    """

    registry = schema_registry()

    # Get meta schema
    here = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(here, 'schema', 'meta-schema.json')) as fp:
        metaschema = json.load(fp)

    validator = Draft202012Validator(metaschema, registry=registry, format_checker=FormatChecker())

    return validator


@pytest.fixture
def bods_validator():
    """
    This sets up and returns the validator, using the statement.json
    schema as the primary schema against which data is validated.
    """

    # Get the registry
    registry = schema_registry()

    # Make the validator
    statement_schema = registry.contents("urn:statement")
    bods_validator = Draft202012Validator(statement_schema, registry=registry, format_checker=FormatChecker())
    return bods_validator


@pytest.fixture
def bods_json(request):
    """
    Returns JSON from a file path.
    This is automatically called on all params for tests which take
    `bods_json` as a parameter with indirect=True, and the output passed to
    the test.
    """
    fp = request.param
    bods = json.loads(fp.read_text())
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
