import os
import pytest
from warnings import warn
from jsonschema.exceptions import ErrorTree
from conftest import get_json_files, file_id, get_test_data_dir

"""
Data tests

Checks that the BODS Schema validates data according to our
expectations.

These tests should be run whenever changes to the schema affect
the validation requirements. New requirements can be tested by
adding new test data files to the /data directory.
"""

valid_bods_statements = get_json_files(os.path.join(get_test_data_dir(), "valid-statements"))
invalid_bods_statements = get_json_files(os.path.join(get_test_data_dir(), "invalid-statements"))


@pytest.mark.parametrize("bods_json", valid_bods_statements, ids=file_id, indirect=True)
def test_valid_files(bods_validator, bods_json):
    file_path, bods = bods_json
    is_valid = bods_validator.is_valid(bods)

    # (temp for debugging)
    if not is_valid:
        errors = bods_validator.iter_errors(bods)
        for error in errors:
            print(error.message)
            print(error.path)
            print(error.schema_path)

    assert is_valid


@pytest.mark.parametrize("bods_json", invalid_bods_statements, ids=file_id, indirect=True)
def test_invalid_files(bods_validator, bods_json, invalid_data_errors):
    file_name, bods = bods_json

    errors = bods_validator.iter_errors(bods)
    tree = ErrorTree(bods_validator.iter_errors(bods))

    # Check file is present in error mapping
    assert file_name in invalid_data_errors.keys(), f"File missing from error mapping, please add it to expected_errors.csv"

    # Should only be one validation error per file
    assert tree.total_errors == 1, f"Expecting 1 validation error, {tree.total_errors} found."

    # Check the type of error and path to the error are what we expect
    for error in errors:
        assert error.validator in invalid_data_errors.get(file_name) and error.json_path in invalid_data_errors.get(
            file_name
        ), f"Expected {invalid_data_errors.get(file_name)[0]} error at {invalid_data_errors.get(file_name)[1]} but found {error.validator} error at {error.json_path}."
        if error.validator == "required":
            assert (
                invalid_data_errors.get(file_name)[2] in error.message
            ), f"Expected {invalid_data_errors.get(file_name)[2]} to be missing, but instead got: {error.message}."

