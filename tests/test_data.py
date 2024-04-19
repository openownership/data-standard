import os
import pytest
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
    error_msgs = ""

    if not is_valid:
        errors = bods_validator.iter_errors(bods)
        for error in errors:
            json_path = "/".join(str(p) for p in error.path)
            schema_path = "/".join(str(p) for p in error.schema_path)
            error_msgs += f"{error.message} at {json_path} (This constraint is in the schema at: {schema_path})"

    assert is_valid, f"Validation failed: {error_msgs}"


@pytest.mark.parametrize("bods_json", invalid_bods_statements, ids=file_id, indirect=True)
def test_invalid_files(bods_validator, bods_json, invalid_data_errors):
    file_name, bods = bods_json

    errors = bods_validator.iter_errors(bods)
    tree = ErrorTree(bods_validator.iter_errors(bods))

    # Check file is present in error mapping
    assert (
        file_name in invalid_data_errors.keys()
    ), "File missing from error mapping, please add it to expected_errors.csv"

    # Should only be one validation error per file
    if tree.total_errors > 1:
        error_msgs = []
        for error in errors:
            error_msgs.append(error.message)
        msgs = "; ".join(error_msgs)
    assert tree.total_errors == 1, f"Expecting 1 validation error, {tree.total_errors} found: {msgs}."

    # Check the type of error and path to the error are what we expect
    for error in errors:
        assert error.validator in invalid_data_errors.get(file_name) and error.json_path in invalid_data_errors.get(
            file_name
        ), f"Expected {invalid_data_errors.get(file_name)[0]} error at {invalid_data_errors.get(file_name)[1]} \
        but found {error.validator} error at {error.json_path}."
        
        if error.validator == "required":
            assert (
                invalid_data_errors.get(file_name)[2] in error.message
            ), f"Expected {invalid_data_errors.get(file_name)[2]} to be missing, but instead got: {error.message}."


def test_error_files_used(invalid_data_errors):
    """
    Check for files in the error mapping which don't exist on disc.
    Not critical to the schema tests, but helps to catch typos and keep the test data tidy.
    """
    for file_name in invalid_data_errors.keys():
        path = os.path.join(get_test_data_dir(), "invalid-statements", file_name)
        assert os.path.isfile(path), f"Unexpected file {file_name} found in expected_errors.csv"
