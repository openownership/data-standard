import os
import json
import pytest

from jscc.testing.checks import (
       validate_array_items,
       validate_codelist_enum,
       validate_deep_properties,
       validate_items_type,
       validate_letter_case,
       validate_metadata_presence,
       validate_null_type,
   )

from pathlib import Path
from jsonschema import FormatChecker
from jsonschema.validators import Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012


def test_metaschema_valid(schema_validator):
    """
    Checks the BODS metaschema is valid against 2020-12.
    check_schema raises a SchemaError if the schema is invalid, so this test
    fails if an error is raised.
    """
    schema_validator.check_schema(schema_validator.schema)


# Set this to a list of the $id values of the schemas you expect to find in the /schema/ directory
schemas = [
    "urn:components",
    "urn:statement",
    "urn:person",
    "urn:entity",
    "urn:relationship"
]

@pytest.mark.parametrize("schema_from_registry", schemas, indirect=True)
def test_schema_valid(schema_validator, schema_from_registry):
    """
    Tests each part of the BODS schema against the BODS metaschema.
    TODO: This only actually validates additional keywords defined when they
    appear at the top level of the schema; see: https://github.com/openownership/data-standard/issues/513
    """
    assert schema_validator.is_valid(schema_from_registry) == True


def test_codelist_enums():
    pass


def test_codelists_used():
    pass


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

