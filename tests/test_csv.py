import csv
import json
import os
import warnings
from io import StringIO

import pytest
from jscc.schema import is_codelist
from jscc.testing.checks import get_invalid_csv_files
from jscc.testing.filesystem import walk_csv_data
from jscc.testing.util import warn_and_assert
from jsonschema import FormatChecker
from jsonschema.validators import Draft4Validator as validator


cwd = os.getcwd()


def formatwarning(message, category, filename, lineno, line=None):
    return str(message).replace(cwd + os.sep, '')


warnings.formatwarning = formatwarning
pytestmark = pytest.mark.filterwarnings('always')


def test_csv_valid():
    warn_and_assert(get_invalid_csv_files(), '{0} is not valid CSV: {1}',
                    'CSV files are invalid. See warnings below.')


def test_valid():
    """
    Ensures all CSV files are valid: no empty rows or columns, no leading or trailing whitespace in cells, same number
    of cells in each row.
    """
    errors = 0

    for path, name, text, fieldnames, rows in walk_csv_data():
        codelist = is_codelist(fieldnames)
        width = len(fieldnames)
        columns = []

        for row_index, row in enumerate(rows, 2):
            if len(row) != width:
                errors += 1
                warnings.warn("ERROR: {} has {} not {} columns in row {}".format(path, len(row), width, row_index))
            if not any(row.values()):
                errors += 1
                warnings.warn("ERROR: {} has empty row {}".format(path, row_index))
            else:
                for col_index, (header, cell) in enumerate(row.items(), 1):
                    if col_index > len(columns):
                        columns.append([])

                    columns[col_index - 1].append(cell)

                    # Extra cells are added to a None columns.
                    if header is None and isinstance(cell, list):
                        cells = cell
                    else:
                        cells = [cell]

                    for cell in cells:
                        if cell is not None and cell != cell.strip():
                            errors += 1
                            warnings.warn(
                                'ERROR: {} {} "{}" has leading or trailing whitespace at {},{}'.format(
                                    path, header, cell, row_index, col_index
                                )
                            )

        # Column 4 (technical note) can be empty, but check the others
        for col_index, column in enumerate(columns, 1):
            if col_index is not 4 and not any(column) and codelist:
                errors += 1
                warnings.warn("ERROR: {} has empty column {}".format(path, col_index))

        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
        expected = output.getvalue()

        if text != expected:
            errors += 1
            warnings.warn(
                "ERROR: {} is improperly formatted (e.g. missing trailing newline, extra quoting "
                'characters, non-"\\n" line terminator):\n{!r}\n{!r}'.format(path, text, expected)
            )

    assert errors == 0, "One or more codelist CSV files are invalid. See warnings below."


def test_codelist():
    """
    Ensures all codelists files are valid against codelist-schema.json.
    """

    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "schema", "codelist-schema.json")
    with open(path) as f:
        codelist_schema = json.load(f)

    any_errors = False

    for path, name, text, fieldnames, rows in walk_csv_data():
        codes_seen = set()
        if is_codelist(fieldnames):
            data = []
            for row_index, row in enumerate(rows, 2):
                code = row["code"]
                if code in codes_seen:
                    any_errors = True
                    warnings.warn('{}: Duplicate code "{}" on row {}'.format(path, code, row_index))
                codes_seen.add(code)

                item = {}
                for k, v in row.items():
                    if k == "code" or v:
                        item[k] = v
                    else:
                        item[k] = None
                data.append(item)

            schema = codelist_schema
            for error in validator(schema, format_checker=FormatChecker()).iter_errors(data):
                any_errors = True
                warnings.warn("{}: {} ({})\n".format(path, error.message, "/".join(error.absolute_schema_path)))

    assert not any_errors
