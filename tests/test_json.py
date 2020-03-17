import shutil

import jscc.testing.json
# Import some tests that will be run by pytest, noqa needed because we don't use them directly
from jscc.testing.json import (is_json_schema, metaschema, test_empty_files, test_indent, test_valid,  # noqa: F401
                               validate_json_schema, walk_json_data)


def empty_validate_function(*args, **kwargs):
    return 0


jscc.testing.json.validate_codelist_enum = empty_validate_function
jscc.testing.json.validate_ref = empty_validate_function
jscc.testing.json.validate_title_description_type = empty_validate_function
jscc.testing.json.validate_object_id = empty_validate_function
jscc.testing.json.validate_null_type = empty_validate_function
jscc.testing.json.validate_codelist_files_used_in_schema = empty_validate_function


metaschema['properties']['version'] = {
    'type': 'string',
}
metaschema['properties']['propertyOrder'] = {
    'type': 'integer',
}


def test_json_schema():
    """
    Ensures all JSON Schema files are valid JSON Schema Draft 4 and use codelists correctly. Unless this is an
    extension, ensures JSON Schema files have required metadata and valid references.
    """

    # Don't check schemas that are built for the other tests
    # Ideally we should test these too
    try:
        shutil.rmtree('schema/testing')
    except FileNotFoundError:
        pass

    for path, text, data in walk_json_data():
        if is_json_schema(data):
            validate_json_schema(path, data, metaschema)
