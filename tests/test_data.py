import os
import pytest
from conftest import get_json_files, file_id

"""
Data tests

Checks that the BODS Schema validates data according to our
expectations.

These tests should be run whenever changes to the schema affect
the validation requirements. New requirements can be tested by
adding new test data files to the /data directory.
"""

valid_bods_statements = get_json_files(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "v0.4", "valid-statements"))
invalid_bods_statements = get_json_files(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "v0.4", "invalid-statements"))


@pytest.mark.parametrize("bods_json", valid_bods_statements, ids=file_id, indirect=True)
def test_valid_files(bods_validator, bods_json):
    is_valid = bods_validator.is_valid(bods_json)

    # (temp for debugging)
    if not is_valid:
        errors = bods_validator.iter_errors(bods_json)
        for error in errors:
            print(error.message)
            print(error.path)
            print(error.schema_path)

    assert is_valid


@pytest.mark.parametrize("bods_json", invalid_bods_statements, ids=file_id, indirect=True)
def test_invalid_files(bods_validator, bods_json):
    is_valid = bods_validator.is_valid(bods_json)

    if not is_valid:
        errors = bods_validator.iter_errors(bods_json)
        for error in errors:
            print(error.message)
            print(error.path)
            print(error.schema_path)

    assert not is_valid
    # todo: assert correct error message and field path


def test_valid_data(bods_validator, get_valid_data):
    is_valid = bods_validator.is_valid(get_valid_data)
    assert is_valid


def test_invalid_data(bods_validator, get_invalid_data):
    is_valid = bods_validator.is_valid(get_invalid_data)
    assert not is_valid
