import glob
import os
import json
import pytest
from collections import OrderedDict
from jsonschema import validate, ValidationError

from bods_validate import this_dir, format_checker, absolute_path_to_schema_dir, resolver
from bods_validate import MissingStatementTypeError, UnrecognisedStatementID
from bods_validate import bods_validate_package, bods_validate_statement
from bods_validate import bods_iter_errors_package, bods_iter_errors_statement, build_schemas_for_testing


# get all json files availiable
files_we_have = []
this_dir_len = len(this_dir) if this_dir.endswith("/") else len(this_dir) + 1
files_we_have.extend([x[this_dir_len:] for x in glob.glob(os.path.join(this_dir, "**", "*.json"), recursive=True)])
files_we_have.extend(
    [x[this_dir_len:] for x in glob.glob(os.path.join(this_dir, "..", "examples", "**/*.json"), recursive=True)]
)
files_by_name = {}
for file in files_we_have:
    file_name = file.split("/")[-1]
    if file_name in files_by_name:
        raise Exception(f"Test file with name {file_name} is already in repo, choose another name for it")
    files_by_name[file_name] = file


def get_full_paths(path_list):
    # This covers the paramitirization formats in this file
    full_paths = []
    for path in path_list:
        if isinstance(path, str):
            full_paths.append(files_by_name[path])

        if isinstance(path, tuple):
            if isinstance(path[0], str):
                full_paths.append((files_by_name[path[0]],) + tuple(path[1:]))
            if isinstance(path[1], list):
                for index, value in enumerate(path[1]):
                    path[1][index] = files_by_name[value]
                full_paths.append(path)
    return full_paths


have_schemas_been_built_for_testing = False


def setup_module(module):
    global have_schemas_been_built_for_testing
    if not have_schemas_been_built_for_testing:
        build_schemas_for_testing()
        have_schemas_been_built_for_testing = True


test_valid_statement_json_parametrize_data = [
    "valid-entity-statement.json",
    "valid-entity-statement-loose-validation.json",
    "valid-entity-statement-with-source.json",
    "valid-person-statement.json",
    "valid-entity-statement-stateBody.json",
    "valid-ownership-or-control-statement.json",
    "gb-coh-entity-statement.json",
    "gb-coh-person-statement.json",
    "natalie-coleman-person-statement.json",
    "ren-consulting-limited-natalie-coleman.json",
    "ren-consulting-limited.json",
    "renco-energy-ltd-entity-statement.json",
    "renco-energy-ltd-roberto-lopez.json",
    "renco-holding-company-limited.json",
    "roberto-lopez.json",
]

test_valid_statement_json_parametrize_data = get_full_paths(test_valid_statement_json_parametrize_data)


@pytest.mark.parametrize("json_path", test_valid_statement_json_parametrize_data)
def test_valid_statement_json(json_path):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f, object_pairs_hook=OrderedDict)
    bods_validate_statement(json_data)


test_valid_package_json_parametrize_data = [
    "valid-bods-package.json",
    "valid-bods-package-entity-owning-entity.json",
    "valid-bods-package-annotations.json",
    "valid-bods-package-linking-annotations.json",
    "gb-coh-bods-package.json",
    "bods-package-ren-consulting-limited.json",
    "1-single-direct.json",
    "2-single-update.json",
    "3-joint-ownership.json",
    "4a-simple-pep-declaration.json",
    "4b-full-pep-declaration.json",
    "os-03-dr-03.json",
    "os-03-dr-04.json",
    "os-06-dr-03.json",
    "os-06-dr-04.json",
    "os-07-dr-04-company-a.json",
    "os-07-dr-04-company-b.json",
    "os-07-dr-04-company-c.json",
    "os-07-dr-04-company-d.json",
    "os-08-dr-04-company-a.json",
    "os-01-dr-01.json",
    "os-01-dr-02-dc-05.json",
    "os-17-dr-02-dc-06.json",
    "valid-entity-statement-plc.json",
    "valid-entity-statement-plc-no-securitiesListings-provided.json",
    "valid-bods-package-fi-soe.json"
]

test_valid_package_json_parametrize_data = get_full_paths(test_valid_package_json_parametrize_data)


@pytest.mark.parametrize("json_path", test_valid_package_json_parametrize_data)
def test_valid_package_json(json_path):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f, object_pairs_hook=OrderedDict)
    assert isinstance(json_data, list)

    # Validate statement by statement
    bods_validate_package(json_data)

    # Validate the whole package at once
    schema_path = "bods-package.json"
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f, object_pairs_hook=OrderedDict)
    validate(json_data, schema, resolver=resolver, format_checker=format_checker)


test_invalid_statement_json_parametrize_data = [
    ("entity-statement-with-invalid-statement-id.json", ValidationError),
    ("entity-statement-with-invalid-statement-id-no-entity-type.json", ValidationError),
    ("entity-statement-extra-field.json", ValidationError),
    ("entity-statement-invalid-date-in-source.json", ValidationError),
    ("entity-statement-no-publication-details.json", ValidationError),
    ("invalid-entity-statement-stateBody-no-entitySubtype-category.json", ValidationError),
    ("person-statement-with-invalid-statement-id.json", ValidationError),
    ("person-statement-with-bad-date.json", ValidationError),
    ("person-statement-no-publication-details.json", ValidationError),
    ("person-statement-no-bods-version.json", ValidationError),
    ("person-statement-no-publication-date.json", ValidationError),
    ("person-statement-no-publisher-sub-prop.json", ValidationError),
    ("person-statement-no-publisher.json", ValidationError),
    ("person-statement-with-bad-bods-version.json", ValidationError),
    ("person-statement-with-bad-licence-url.json", ValidationError),
    ("person-statement-with-bad-publication-date.json", ValidationError),
    ("person-statement-with-bad-publisher-url.json", ValidationError),
    ("ownership-or-control-statement-with-invalid-statement-id.json", ValidationError),
    ("ownership-or-control-statement-no-publication-details.json", ValidationError),
    ("ownership-or-control-statement-no-statement-type.json", MissingStatementTypeError),
    ("ownership-or-control-statement-no-url-linking-annotation.json", ValidationError),
]

test_invalid_statement_json_parametrize_data = get_full_paths(test_invalid_statement_json_parametrize_data)


@pytest.mark.parametrize(("json_path", "error"), test_invalid_statement_json_parametrize_data)
def test_invalid_statement_json(json_path, error):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f, object_pairs_hook=OrderedDict)
    with pytest.raises(error):
        bods_validate_statement(json_data)


test_invalid_package_json_parametrize_data = [
    (
        None,
        [
            "valid-entity-statement.json",
            "valid-entity-statement-loose-validation.json",
            "valid-person-statement.json",
            "ownership-or-control-statement-with-invalid-statement-id.json",
        ],
        ValidationError,
    ),
    (
        None,
        [
            "valid-entity-statement.json",
            "valid-entity-statement-loose-validation.json",
            "valid-person-statement.json",
            "ownership-or-control-statement-no-statement-type.json",
        ],
        MissingStatementTypeError,
    ),
    ("bods-package-missing-entity-statement.json", None, UnrecognisedStatementID),
    ("bods-package-incorrect-ordering.json", None, UnrecognisedStatementID),
]

test_invalid_package_json_parametrize_data = get_full_paths(test_invalid_package_json_parametrize_data)


@pytest.mark.parametrize(("json_path", "json_paths", "error"), test_invalid_package_json_parametrize_data)
def test_invalid_package_json(json_path, json_paths, error):
    if json_path:
        with open(os.path.join(this_dir, json_path)) as f:
            json_data = json.load(f, object_pairs_hook=OrderedDict)
    else:
        json_data = [json.load(open(os.path.join(this_dir, json_path))) for json_path in json_paths]

    # Validate statement by statement
    with pytest.raises(error):
        bods_validate_package(json_data)

    # We don't get unrecognised statement errors if we validate the whole
    # package
    if error is UnrecognisedStatementID:
        return

    # Validate the whole package at once
    schema_path = "bods-package.json"
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f, object_pairs_hook=OrderedDict)
    with pytest.raises(ValidationError):
        validate(json_data, schema, resolver=resolver, format_checker=format_checker)


test_invalid_statement_json_iter_errors_parametrize_data = [
    ("valid-entity-statement.json", set()),
    ("valid-entity-statement-loose-validation.json", set()),
    ("valid-entity-statement-transliteration-annotations.json", set()),
    ("valid-person-statement.json", set()),
    ("valid-ownership-or-control-statement.json", set()),
    ("entity-statement-with-invalid-statement-id.json", {"'too-short-so-fail' is too short"}),
    (
        "entity-statement-with-invalid-statement-id-no-entity-type.json",
        {
            "'too-short-so-fail' is too short",
            "'entityType' is a required property",
        },
    ),
    (
        "entity-statement-no-publication-details.json",
        {
            "'publicationDetails' is a required property",
            "Additional properties are not allowed ('publicationDetailsTypo' was unexpected)",
        },
    ),
    (
        "ownership-or-control-statement-no-publication-details.json",
        {
            "'publicationDetails' is a required property",
            "Additional properties are not allowed ('publicationDetailsTypo' was unexpected)",
        },
    ),
    (
        "person-statement-no-publication-details.json",
        {
            "'publicationDetails' is a required property",
            "Additional properties are not allowed ('publicationDetailsTypo' was unexpected)",
        },
    ),
    ("person-statement-with-invalid-statement-id.json", {"'too-short-so-fail' is too short"}),
    (
        "person-statement-with-bad-date.json",
        {
            "'Tuesday' is not a 'date'",
        },
    ),
    (
        "person-statement-no-bods-version.json",
        {
            "'bodsVersion' is a required property",
            "Additional properties are not allowed ('bodsVersionTypo' was unexpected)",
        },
    ),
    (
        "person-statement-no-publication-date.json",
        {
            "'publicationDate' is a required property",
            "Additional properties are not allowed ('publicationDateTypo' was unexpected)",
        },
    ),
    (
        "person-statement-no-publisher-sub-prop.json",
        {
            "OrderedDict([('nameTypo', 'CHRINON LTD')]) is not valid under any of the given schemas",
            "Additional properties are not allowed ('nameTypo' was unexpected)",
        },
    ),
    (
        "person-statement-no-publisher.json",
        {
            "'publisher' is a required property",
            "Additional properties are not allowed ('publisherTypo' was unexpected)",
        },
    ),
    (
        "person-statement-with-bad-bods-version.json",
        {
            "'1' does not match '^(\\\\d+\\\\.)(\\\\d+)$'",
        },
    ),
    (
        "person-statement-with-bad-licence-url.json",
        {
            "'exampledotcom' is not a 'uri'",
        },
    ),
    (
        "person-statement-with-bad-publication-date.json",
        {
            "'2017/11/18' is not a 'date'",
        },
    ),
    (
        "person-statement-with-bad-publisher-url.json",
        {
            "'CHRINON LTD' is not a 'uri'",
        },
    ),
    (
        "entity-statement-invalid-date-in-source.json",
        {
            "'2018-11-14' is not a 'date-time'",
        },
    ),
    (
        "ownership-or-control-statement-with-invalid-statement-id.json",
        {
            "'too-short-so-fail' is too short",
        },
    ),
    (
        "ownership-or-control-statement-no-statement-type.json",
        {
            "'statementType' is a required property",
        },
    ),
    (
        "invalid-entity-statement-stateBody-no-entitySubtype-category.json",
        {
            "'generalCategory' is a required property",
        },
    ),
]

test_invalid_statement_json_iter_errors_parametrize_data = get_full_paths(
    test_invalid_statement_json_iter_errors_parametrize_data
)


@pytest.mark.parametrize(("json_path", "expected_errors"), test_invalid_statement_json_iter_errors_parametrize_data)
def test_invalid_statement_json_iter_errors(json_path, expected_errors):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f, object_pairs_hook=OrderedDict)
    actual_errors = {e.message for e in bods_iter_errors_statement(json_data)}
    assert actual_errors == expected_errors


test_invalid_package_json_iter_errors_parametrize_data = [
    ("valid-bods-package.json", None, set()),
    ("valid-bods-package-annotations.json", None, set()),
    ("valid-bods-package-linking-annotations.json", None, set()),
    (
        None,
        [
            "valid-entity-statement.json",
            "valid-person-statement.json",
            "ownership-or-control-statement-with-invalid-statement-id.json",
        ],
        {"'too-short-so-fail' is too short"},
    ),
    (
        None,
        [
            "valid-entity-statement.json",
            "valid-person-statement.json",
            "ownership-or-control-statement-no-statement-type.json",
        ],
        {
            "'statementType' is a required property",
        },
    ),
    (
        None,
        [
            "entity-statement-loose-validation-without-required-fields.json",
        ],
        {
            "OrderedDict([('id', '00335'), ('register', 'Jebel Ali Free Zone')]) is not valid under any of the given schemas",
            "Additional properties are not allowed ('register' was unexpected)",
        },
    ),
    (
        "bods-package-missing-entity-statement.json",
        None,
        {
            "subject/describedByEntityStatement '1dc0e987-5c57-4a1c-b3ad-61353b66a9b7' does not match any known entities"
        },
    ),
    (
        "bods-package-missing-interested-party-entity-statement.json",
        None,
        {
            "interestedParty/describedByEntityStatement 'd36e6807-020c-4fb5-a0d4-5ab9eb971514' does not match any known entities"
        },
    ),
    (
        "bods-package-incorrect-ordering.json",
        None,
        {
            "interestedParty/describedByPersonStatement '019a93f1-e470-42e9-957b-03559861b2e2' does not match any known persons"
        },
    ),
    ("invalid-entity-statement-no-securitiesListings.json", None, {"'securitiesListings' is a required property"}),
    (
        "invalid-entity-statement-plc-invalid-idScheme.json",
        None,
        {"'local' is not one of ['isin', 'figi', 'cusip', 'cins']"},
    ),
    ("invalid-entity-statement-plc-no-security.json", None, {"'security' is a required property"}),
    (
        "invalid-entity-statement-plc-no-stockExchangeJurisdiction.json",
        None,
        {"'stockExchangeJurisdiction' is a required property"},
    ),
    ("invalid-entity-statement-plc-no-stockExchangeName.json", None, {"'stockExchangeName' is a required property"}),
    ("invalid-entity-statement-plc-no-ticker.json", None, {"'ticker' is a required property"}),
]

test_invalid_package_json_iter_errors_parametrize_data = get_full_paths(
    test_invalid_package_json_iter_errors_parametrize_data
)


@pytest.mark.parametrize(
    ("json_path", "json_paths", "expected_errors"), test_invalid_package_json_iter_errors_parametrize_data
)
def test_invalid_package_json_iter_errors(json_path, json_paths, expected_errors):
    if json_path:
        with open(os.path.join(this_dir, json_path)) as f:
            json_data = json.load(f, object_pairs_hook=OrderedDict)
    else:
        json_data = [
            json.load(open(os.path.join(this_dir, json_path)), object_pairs_hook=OrderedDict)
            for json_path in json_paths
        ]
    actual_errors = {e.message for e in bods_iter_errors_package(json_data)}
    assert actual_errors == expected_errors


def test_all_examples_and_data_files_are_used():
    # get all files we use in tests
    files_used = []
    files_used.extend(test_valid_statement_json_parametrize_data)
    files_used.extend(test_valid_package_json_parametrize_data)
    files_used.extend([a[0] for a in test_invalid_statement_json_parametrize_data])
    files_used.append('schema/meta-schema.json')
    for data in test_invalid_package_json_parametrize_data:
        if data[0]:
            files_used.append(data[0])
        elif data[1]:
            files_used.extend(data[1])
    files_used.extend([a[0] for a in test_invalid_statement_json_iter_errors_parametrize_data])

    for data in test_invalid_package_json_iter_errors_parametrize_data:
        if data[0]:
            files_used.append(data[0])
        elif data[1]:
            files_used.extend(data[1])
    # make sure all files are used
    files_we_have_but_dont_use = set(files_we_have) - set(files_used)
    assert files_we_have_but_dont_use == set()
