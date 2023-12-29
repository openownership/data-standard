import os
import pytest

from fixtures import bods_json, bods_validator, file_id, get_json_files, get_invalid_data, get_valid_data

valid_bods_statements = get_json_files(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "v0.4", "valid-statements"))

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

    assert is_valid == True

def test_valid_data(bods_validator, get_valid_data):
    is_valid = bods_validator.is_valid(get_valid_data)
    assert is_valid == True

def test_invalid_data(bods_validator, get_invalid_data):
    is_valid = bods_validator.is_valid(get_valid_data)
    assert is_valid == False

