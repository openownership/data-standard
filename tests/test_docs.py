import pytest
import warnings

from conftest import get_json_files, get_examples_dir, file_id
from jscc.testing.checks import get_empty_files, get_misindented_files, get_invalid_json_files


"""
Docs tests

Checks the example data used in the documentation are all valid BODS.
"""


examples = get_json_files(get_examples_dir())


def test_examples_empty(examples_dir):
    """
    Check the data in the /examples directory are not empty
    """
    errors = False
    empties = get_empty_files(top=examples_dir)
    for path in empties:
        warnings.warn(f"ERROR: Empty file at {path}", stacklevel=1)
        errors = True

    assert not errors, "Empty files found, see warnings."


def test_examples_indent(examples_dir):
    """
    Check the data in the /examples directory are indented correctly.
    """
    errors = False
    misindented = get_misindented_files(top=examples_dir)
    for path in misindented:
        warnings.warn(f"ERROR: Misindented files at {path}", stacklevel=1)
        errors = True

    assert not errors, "Misindented files found, see warnings."


def test_examples_valid_json(examples_dir):
    """
    Check data in /examples director are valid JSON files.
    """
    errors = False
    invalid = get_invalid_json_files(top=examples_dir)
    for path in invalid:
        warnings.warn(f"ERROR: Invalid JSON at {path}", stacklevel=1)
        errors = True

    assert not errors, "Invalid JSON found, see warnings."


@pytest.mark.parametrize("bods_json", examples, ids=file_id, indirect=True)
def test_examples_valid_bods(bods_validator, bods_json):
    """
    Check data in /examples directory are valid BODS.
    """
    file_name, bods = bods_json
    is_valid = bods_validator.is_valid(bods)

    error_msgs = []
    if not is_valid:
        errors = bods_validator.iter_errors(bods)
        for error in errors:
            error_msgs.append(error.message)

    error_msgs = "; ".join(error_msgs)

    assert is_valid, f"Validation error: {error_msgs}"
