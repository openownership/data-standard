import pytest

from conftest import codelist_paths, codelist_id, schema_paths
from jscc.testing.checks import (
    validate_array_items,
    validate_codelist_enum,
    validate_deep_properties,
    validate_items_type,
    validate_letter_case,
    validate_metadata_presence,
    validate_null_type,
)


"""
Schema tests

Checks that the BODS schema files (JSON and CSV) are valid and complete.

These tests should be run whenever changes to the schema files are made.
The `schemas` variable should be updated if a new JSON schema file is
added to or removed from the /schema directory, or if any of the schema
components are renamed.
"""


# Set `schemas` to a list of the $id values of the schemas you expect to find in the /schema/ directory
schemas = [
    "urn:components",
    "urn:statement",
    "urn:person",
    "urn:entity",
    "urn:relationship",
    "urn:codelists"
]


codelists = codelist_paths()


def test_metaschema_valid(schema_validator):
    """
    Checks the BODS metaschema is valid against 2020-12.
    check_schema raises a SchemaError if the schema is invalid, so this test
    fails if an error is raised.
    """
    schema_validator.check_schema(schema_validator.schema)


def test_schemas_loaded():
    # check schemas var matches number of files in schema dir
    schemas_from_file = schema_paths()
    assert len(schemas_from_file) == len(schemas), "Schema found on disc that is not being tested.\nPlease update the schemas variable in test_schema.py."


@pytest.mark.parametrize("schema_from_registry", schemas, indirect=True)
def test_schema_valid(schema_validator, schema_from_registry):
    """
    Tests each part of the BODS schema against the BODS metaschema.
    TODO: This only actually validates additional keywords defined when they
    appear at the top level of the schema; see: https://github.com/openownership/data-standard/issues/513
    """
    assert schema_validator.is_valid(schema_from_registry) is True


def test_letter_case():
    """
    Tests that properties are lowerCamelCase and definition names are
    UpperCamelCase.
    """
    # errors = validate_letter_case(path, data)
    # assert errors == None
    pass


def test_items_type():
    # validate_items_type(path, data)
    pass


def test_null_type():
    # validate_null_type(path, data)
    pass


def test_array_items():
    # validate_array_items(path, data)
    pass


def test_field_metadata():
    # validate_metadata_presence(path, data)
    pass


@pytest.mark.parametrize("codelist_json", codelists, ids=codelist_id, indirect=True)
def test_codelists_valid(codelist_json, codelist_validator):
    """
    Validate the codelists against the codelist-schema. Checks:
     * No empty values where not allowed (therefore no empty rows or columns,
       same number of cells in each row).
     * Column headers are only the allowed ones (no extras).
     * Values don't have leading or trailing whitespace.
    """
    any_errors = False
    error_str = ''
    errors = codelist_validator.iter_errors(codelist_json)
    for error in errors:
        any_errors = True
        error_str += '\n%s: %s' % (error.path, error.message)

    assert not any_errors, error_str


@pytest.mark.parametrize("codelist_json", codelists, ids=codelist_id, indirect=True)
def test_duplicate_codes(codelist_json):
    """
    Check that codes are not duplicated within a codelist file.
    """
    codes = [row['code'] for row in codelist_json]
    codes.sort()  # sort for readability in the error message
    unique_codes = set(codes)
    assert len(codes) == len(unique_codes), "Duplicate codes found: %s" % (codes)


def test_codelist_enums():
    # check csv codelists match enums in schema json
    pass


def test_codelists_used():
    # check there are no codelist csvs not present in the schema
    # and that there are no codelists in schema missing csvs
    pass
