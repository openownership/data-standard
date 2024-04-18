import pytest
import collections

from conftest import get_codelist_paths, codelist_id, get_schema_paths, validate_metadata_presence
from jscc.testing.checks import (
    validate_array_items,
    validate_items_type,
    validate_letter_case,
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
schemas = ["urn:components", "urn:statement", "urn:person", "urn:entity", "urn:relationship", "urn:codelists"]


schema_paths = get_schema_paths()
codelists = get_codelist_paths()


def test_metaschema_valid(schema_validator):
    """
    Checks the BODS metaschema is valid against 2020-12.
    check_schema raises a SchemaError if the schema is invalid, so this test
    fails if an error is raised.
    """
    schema_validator.check_schema(schema_validator.schema)


def test_schemas_loaded():
    # check schemas var matches number of files in schema dir
    schemas_from_file = get_schema_paths()
    assert len(schemas_from_file) == len(
        schemas
    ), ("Schema found on disc that is either not valid JSON or not being tested.\n"
        "Please fix the JSON or update the schemas variable in test_schema.py.")


@pytest.mark.parametrize("schema_from_registry", schemas, indirect=True)
def test_schema_valid(schema_validator, schema_from_registry):
    """
    Tests each part of the BODS schema against the BODS metaschema.
    TODO: This only actually validates additional keywords defined when they
    appear at the top level of the schema; see: https://github.com/openownership/data-standard/issues/513
    """
    assert schema_validator.is_valid(schema_from_registry)


@pytest.mark.parametrize("schema_from_registry", schemas, indirect=True)
def test_letter_case(schema_from_registry):
    """
    Tests that properties are lowerCamelCase and definition names are
    UpperCamelCase.
    """
    if schema_from_registry.get("$id") != "urn:codelists":
        # codelist schema is excluded from this check because 'technical note' is used instead of technicalNote
        errors = validate_letter_case(schema_from_registry.get("$id"), schema_from_registry)
        assert errors == 0


@pytest.mark.parametrize("schema_from_registry", schemas, indirect=True)
def test_items_type(schema_from_registry):
    """
    Tests that the `type` value of items in an array are allowed. Allowed types:
    * array
    * number
    * string
    * object
    """
    errors = validate_items_type(
        schema_from_registry.get("$id"), schema_from_registry, additional_valid_types=["object"]
    )
    assert errors == 0


@pytest.mark.parametrize("schema_from_registry", schemas, indirect=True)
def test_null_type(schema_from_registry):
    """
    Tests that no field in the schema allows a null value.
    `technical note` in the codelists schema is excluded from this, as that can be empty.
    """
    errors = validate_null_type(
        schema_from_registry.get("$id"),
        schema_from_registry,
        no_null=True,
        allow_null=["/items/properties/technical note"],
    )
    assert errors == 0


@pytest.mark.parametrize("schema_from_registry", schemas, indirect=True)
def test_array_items(schema_from_registry):
    """
    Tests that all fields which can be arrays set the `items` property.
    """
    errors = validate_array_items(schema_from_registry.get("$id"), schema_from_registry)
    assert errors == 0


@pytest.mark.parametrize("schema_from_registry", schemas, indirect=True)
def test_field_metadata(schema_from_registry):
    """
    Tests that all fields have a `title` and `description` property unless they are `$ref`s.
    """
    errors = validate_metadata_presence(schema_from_registry.get("$id"), schema_from_registry)
    assert errors == 0, f"{errors} fields missing title or description fields, see warnings."


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
    error_str = ""
    errors = codelist_validator.iter_errors(codelist_json)
    for error in errors:
        any_errors = True
        error_str += f"\n{error.path}: {error.message}"

    assert not any_errors, error_str


@pytest.mark.parametrize("codelist_json", codelists, ids=codelist_id, indirect=True)
def test_duplicate_codes(codelist_json):
    """
    Check that codes are not duplicated within a codelist file.
    """
    codes = [row["code"] for row in codelist_json]
    codes.sort()  # sort for readability in the error message
    unique_codes = set(codes)
    assert len(codes) == len(unique_codes), f"Duplicate codes found: {codes}"


@pytest.mark.parametrize("codelist_enums", schemas, indirect=True)
def test_schema_codelists_match(codelist_enums):
    """
    Check the codes in the CSV codelist files match the respective enums in the JSON schema
    """
    any_errors = False
    error_str = ""
    for _, name, _, _, rows in codelists:
        codes = [row["code"] for row in rows]
        if codelist_enums.get(name):
            if collections.Counter(codelist_enums.get(name)) != collections.Counter(codes):
                any_errors = True
                error_str += (
                    f"\nCodelist file and schema enum mismatch:\n{name}: {codes}\nenum: {codelist_enums.get(name)}"
                )

    assert not any_errors, error_str


def test_schema_codelists_used(codelist_values):
    """
    Check there are no codelist csvs not present in the schema
    and that there are no codelists in schema missing csvs.

    The `validate_schema_codelists_match` function in jscc doesn't work here
    because it can only handle one schema file.
    """
    codelist_files = [name for _, name, _, _, _ in codelists]
    unused_codelists = [codelist for codelist in codelist_files if codelist not in codelist_values]
    missing_codelists = [codelist for codelist in codelist_values if codelist not in codelist_files]

    assert len(unused_codelists) == 0, f"Codelist files which are not used in the schema: {unused_codelists}"
    assert (
        len(missing_codelists) == 0
    ), f"Codelists used in schema for which there are no CSV files: {missing_codelists}"
