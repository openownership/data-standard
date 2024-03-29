import os
import csv
import json
import pytest

from warnings import warn
from pathlib import Path
from jsonschema import FormatChecker
from jsonschema.validators import Draft202012Validator
from jscc.schema import is_json_schema, is_codelist, is_missing_property
from jscc.exceptions import MetadataPresenceWarning
from jscc.testing.checks import _false, _traverse
from jscc.testing.filesystem import walk_json_data, walk_csv_data
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012


"""
The fixtures in this file are automatically discovered by pytest without
needing to import them in the test files.

After the pytest fixtures are helper functions used by the fixtures, or
sometimes the tests directly.
"""


@pytest.fixture
def schema_dir():
    """
    Makes the directory the schema files are in available to tests.
    """
    return get_schema_dir()


@pytest.fixture
def codelists_dir():
    """
    Makes the directory the codeslists are in available to tests.
    """
    return os.path.join(get_schema_dir(), "codelists")


@pytest.fixture
def examples_dir():
    """
    Makes the directory the example files are in available to tests.
    """
    return get_examples_dir()


@pytest.fixture
def schema_from_registry(request):
    """
    Fetches a schema from the registry by id.
    `request.param` should be the value of `$id` in the schema.
    """
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
    with open(os.path.join(here, "schema", "meta-schema.json")) as fp:
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
def codelist_validator():
    """
    This sets up and returns a validator for the codelists schema.
    """
    # Get the registry
    registry = schema_registry()

    # Make the validator
    codelist_schema = registry.contents("urn:codelists")
    codelist_validator = Draft202012Validator(codelist_schema, registry=registry, format_checker=FormatChecker())
    return codelist_validator


@pytest.fixture
def bods_json(request):
    """
    Returns a tuple of filename and JSON from a file path.
    This is automatically called on all params for tests which take
    `bods_json` as a parameter with indirect=True, and the output passed to
    the test.
    """
    fp = request.param
    bods = json.loads(fp.read_text())
    return (fp.name, bods)


@pytest.fixture
def codelist_json(request):
    """
    Returns JSON version of a codelist from a CSV file path.
    This is automatically called on all params for tests which take
    `codelist_json` as a parameter with indirect=True, and the output passed to
    the test.
    """
    codelist = request.param  # (path, name, text, fieldnames, rows)
    return codelist[4]


@pytest.fixture
def codelist_values():
    """
    Parses the schema for `codelist` fields and returns the values
    (eg. 'entityType.csv') of those fields.
    Checks all schema files at once and returns a list of all codelist values seen.
    """
    codelists = {}
    schema_paths = get_schema_paths()
    for _, _, data in schema_paths:
        codelists.update(get_codelists_from_schema(data))

    codelist_names = list(codelists.keys())
    return codelist_names


@pytest.fixture
def codelist_enums(request):
    """
    Parses the schema for `codelist` fields and retrieves the accompanying `enum` value.
    Expects the value of the schema `$id` field to be passed from the test,
    and only gets values from the one schema.
    """
    registry = schema_registry()
    schema_contents = registry.contents(request.param)
    return get_codelists_from_schema(schema_contents)


@pytest.fixture
def invalid_data_errors():
    """
    The CSV file expected_errors.csv maps the invalid test data filenames to the expected validation errors.
    This function reads that file into a dict with structure:
        { file_name: ( validation_error, json_path, property ) }
    for use in the invalid data tests.
    Update the CSV file when new invalid data files are created.
    """
    errors = {}
    with open(os.path.join(get_test_data_dir(), "invalid-statements", "expected_errors.csv"), newline="") as csvfile:
        r = csv.reader(csvfile, delimiter=",", quotechar='"')
        for row in r:
            errors[row[0]] = (row[1], row[2], row[3])

    return errors


def get_json_files(dir):
    """
    Recursively gets files with .json extension in `path` and returns
    a list of the full paths.
    """
    paths = []
    for p in Path(dir).rglob("*.json"):
        paths.append(p)
    return paths


def file_id(path):
    """
    Return the file name from a path; helps with
    understanding test errors.
    """
    return path.name


def codelist_id(codelist_data):
    """
    Return the file name of a codelist from the path data; helps with
    understanding test errors.
    codelist_data is (path, name, text, fieldnames, rows)
    """
    return codelist_data[1]


def get_schema_dir():
    """
    Assumes the schema directory is /schema
    """
    here = os.path.dirname(os.path.realpath(__file__))
    schema_dir = os.path.join(here, "..", "schema")
    return schema_dir


def get_examples_dir():
    """
    Assumes the examples directory is /examples
    """
    here = os.path.dirname(os.path.realpath(__file__))
    schema_dir = os.path.join(here, "..", "examples")
    return schema_dir


def get_test_data_dir():
    """
    Assumes the data for the tests is in /tests/data
    """
    here = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(here, "data")
    return data_dir


def get_schema_paths():
    """
    Returns an array of paths, filenames, and contents (parsed JSON) for each of the schema files.
    """
    schema_dir = get_schema_dir()
    schema_paths = [
        (path, name, data) for path, name, _, data in walk_json_data(top=schema_dir) if is_json_schema(data)
    ]
    return schema_paths


def get_codelist_paths():
    """
    Returns an array of paths, filenames and contents for each codelist in the codelists directory.
    """
    codelists_dir = os.path.join(get_schema_dir(), "codelists")
    codelist_paths = [
        (path, name, text, fieldnames, rows)
        for path, name, text, fieldnames, rows in walk_csv_data(top=codelists_dir)
        if is_codelist(fieldnames)
    ]
    return codelist_paths


def schema_registry():
    """
    This loads the BODS schema files into a jsonschema registry, so the
    validator can resolve $refs across all of the schema files.
    """
    schemas = []
    for _, _, schema in get_schema_paths():
        schemas.append((schema.get("$id"), Resource(contents=schema, specification=DRAFT202012)))

    registry = Registry().with_resources(schemas)
    return registry


def get_codelists_from_schema(schema_content, pointer=""):
    """
    Gets the value of `codelist` properties and accompanying `enum`s from the schema.
    Adapted from JSCC: https://github.com/open-contracting/jscc/blob/main/jscc/testing/checks.py#L696C5-L712C25
    """
    codelists = {}

    if isinstance(schema_content, list):
        for index, item in enumerate(schema_content):
            codelists.update(get_codelists_from_schema(item, pointer=f"{pointer}/{index}"))
    elif isinstance(schema_content, dict):
        if "codelist" in schema_content:
            codelists[schema_content.get("codelist")] = schema_content.get("enum")

        for key, value in schema_content.items():
            codelists.update(get_codelists_from_schema(value, pointer=f"{pointer}/{key}"))

    return codelists


def validate_metadata_presence(*args, allow_missing=_false):
    """
    Warns and returns the number of errors relating to metadata in a JSON Schema.

    The root schema and each field must have `"type" <https://tools.ietf.org/html/draft-fge-json-schema-validation-00#section-5.5.2>`__,
    `"title" and "description" <https://tools.ietf.org/html/draft-fge-json-schema-validation-00#section-6.1>`__
    properties, unless it has a `"$ref" <https://tools.ietf.org/html/draft-pbryan-zyp-json-ref-03>`__ property.

    :param function allow_missing: a method that accepts a JSON Pointer, and returns whether the field is allowed to
                                   not have a "title" or "description" property
    :returns: the number of errors
    :rtype: int

    This is copied from JSCC to patch oneOf/anyOf/allOf/if/then/else properties being flagged by this.
    TODO: see if this should be fixed in JSCC directly.
    """  # noqa: E501
    schema_fields = {
        "definitions",
        "$defs",
        "deprecated",
        "items",
        "patternProperties",
        "properties",
        "oneOf",
        "anyOf",
        "allOf",
        "if",
        "then",
        "else",
    }
    schema_sections = {"patternProperties", "properties", "anyOf", "allOf", "if", "then", "else", "oneOf"}
    required_properties = {"title", "description"}

    def block(path, data, pointer):
        errors = 0

        parts = pointer.rsplit("/")
        if len(parts) >= 3:
            grandparent = parts[-2]
        else:
            grandparent = None
        parent = parts[-1]

        # Look for metadata fields on user-defined objects only. (Add exceptional condition for "items" field.)
        if parent not in schema_fields and grandparent not in schema_sections:
            for prop in required_properties:
                # If a field has `$ref`, then its `title` and `description` might defer to the reference.
                if is_missing_property(data, prop) and "$ref" not in data and not allow_missing(pointer):
                    errors += 1
                    warn(f'{path} is missing "{prop}" at {pointer}', MetadataPresenceWarning)

            if (
                "type" not in data
                and "$ref" not in data
                and "oneOf" not in data
                and "$defs" not in data
                and not allow_missing(pointer)
            ):
                errors += 1
                warn(f'{path} is missing "type" or "$ref" or "oneOf" at {pointer}', MetadataPresenceWarning)

        return errors

    return _traverse(block)(*args)
