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


have_schemas_been_built_for_testing = False


def setup_module(module):
    global have_schemas_been_built_for_testing
    if not have_schemas_been_built_for_testing:
        build_schemas_for_testing()
        have_schemas_been_built_for_testing = True


test_valid_statement_json_parametrize_data = [
    'data/entity-statement/valid/valid-entity-statement.json',
    'data/entity-statement/valid/valid-entity-statement-loose-validation.json',
    'data/entity-statement/valid/valid-entity-statement-with-source.json',
    'data/person-statement/valid/valid-person-statement.json',
    'data/ownership-or-control-statement/valid/valid-ownership-or-control-statement.json',
    '../examples/flat-serialisation/gb-coh-entity-statement.json',
    '../examples/flat-serialisation/gb-coh-person-statement.json',
    '../examples/workshop/modelling-bods-data/natalie-coleman-person-statement.json',
    '../examples/workshop/modelling-bods-data/ren-consulting-limited-natalie-coleman.json',
    '../examples/workshop/modelling-bods-data/ren-consulting-limited.json',
    '../examples/workshop/modelling-bods-data/renco-energy-ltd-entity-statement.json',
    '../examples/workshop/modelling-bods-data/renco-energy-ltd-roberto-lopez.json',
    '../examples/workshop/modelling-bods-data/renco-holding-company-limited.json',
    '../examples/workshop/modelling-bods-data/roberto-lopez.json'
]


@pytest.mark.parametrize('json_path', test_valid_statement_json_parametrize_data)
def test_valid_statement_json(json_path):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f, object_pairs_hook=OrderedDict)
    bods_validate_statement(json_data)


test_valid_package_json_parametrize_data = [
    'data/bods-package/valid/valid-bods-package.json',
    'data/bods-package/valid/valid-bods-package-entity-owning-entity.json',
    'data/bods-package/valid/valid-bods-package-annotations.json',
    'data/bods-package/valid/valid-bods-package-linking-annotations.json',
    '../examples/flat-serialisation/gb-coh-bods-package.json',
    '../examples/workshop/modelling-bods-data/bods-package-ren-consulting-limited.json',
    '../examples/1-single-direct.json',
    '../examples/2-single-update.json',
    '../examples/3-joint-ownership.json',
    '../examples/4a-simple-pep-declaration.json',
    '../examples/4b-full-pep-declaration.json',
    '../examples/indirect-ownership/os-03-dr-03.json',
    '../examples/indirect-ownership/os-03-dr-04.json',
    '../examples/indirect-ownership/os-06-dr-03.json',
    '../examples/indirect-ownership/os-06-dr-04.json',
    '../examples/indirect-ownership/os-07-dr-04-company-a.json',
    '../examples/indirect-ownership/os-07-dr-04-company-b.json',
    '../examples/indirect-ownership/os-07-dr-04-company-c.json',
    '../examples/indirect-ownership/os-07-dr-04-company-d.json',
    '../examples/indirect-ownership/os-08-dr-04-company-a.json',
    '../examples/os-01-dr-01.json',
    '../examples/missing-data/os-01-dr-02-dc-05.json',
    '../examples/missing-data/os-17-dr-02-dc-06.json'
]


@pytest.mark.parametrize('json_path', test_valid_package_json_parametrize_data)
def test_valid_package_json(json_path):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f, object_pairs_hook=OrderedDict)
    assert isinstance(json_data, list)

    # Validate statement by statement
    bods_validate_package(json_data)

    # Validate the whole package at once
    schema_path = 'bods-package.json'
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f, object_pairs_hook=OrderedDict)
    validate(json_data, schema, resolver=resolver, format_checker=format_checker)


test_invalid_statement_json_parametrize_data = [
    ('data/entity-statement/invalid/entity-statement-with-invalid-statement-id.json', ValidationError),
    ('data/entity-statement/invalid/entity-statement-with-invalid-statement-id-no-entity-type.json', ValidationError),
    ('data/entity-statement/invalid/entity-statement-extra-field.json', ValidationError),
    ('data/entity-statement/invalid/entity-statement-invalid-date-in-source.json', ValidationError),
    ('data/entity-statement/invalid/entity-statement-no-publication-details.json', ValidationError),
    ('data/person-statement/invalid/person-statement-with-invalid-statement-id.json', ValidationError),
    ('data/person-statement/invalid/person-statement-with-bad-date.json', ValidationError),
    ('data/person-statement/invalid/person-statement-no-publication-details.json', ValidationError),
    ('data/person-statement/invalid/person-statement-no-bods-version.json', ValidationError),
    ('data/person-statement/invalid/person-statement-no-publication-date.json', ValidationError),
    ('data/person-statement/invalid/person-statement-no-publisher-sub-prop.json', ValidationError),
    ('data/person-statement/invalid/person-statement-no-publisher.json', ValidationError),
    ('data/person-statement/invalid/person-statement-with-bad-bods-version.json', ValidationError),
    ('data/person-statement/invalid/person-statement-with-bad-licence-url.json', ValidationError),
    ('data/person-statement/invalid/person-statement-with-bad-publication-date.json', ValidationError),
    ('data/person-statement/invalid/person-statement-with-bad-publisher-url.json', ValidationError),
    ('data/ownership-or-control-statement/invalid/ownership-or-control-statement-with-invalid-statement-id.json', ValidationError),
    ('data/ownership-or-control-statement/invalid/ownership-or-control-statement-no-publication-details.json', ValidationError),
    ('data/ownership-or-control-statement/invalid/ownership-or-control-statement-no-statement-type.json', MissingStatementTypeError),
    ('data/ownership-or-control-statement/invalid/ownership-or-control-statement-no-url-linking-annotation.json', ValidationError),
]


@pytest.mark.parametrize(('json_path', 'error'), test_invalid_statement_json_parametrize_data)
def test_invalid_statement_json(json_path, error):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f, object_pairs_hook=OrderedDict)
    with pytest.raises(error):
        bods_validate_statement(json_data)


test_invalid_package_json_parametrize_data = [
    (None, [
        'data/entity-statement/valid/valid-entity-statement.json',
        'data/entity-statement/valid/valid-entity-statement-loose-validation.json',
        'data/person-statement/valid/valid-person-statement.json',
        'data/ownership-or-control-statement/invalid/ownership-or-control-statement-with-invalid-statement-id.json'
    ], ValidationError),
    (None, [
        'data/entity-statement/valid/valid-entity-statement.json',
        'data/entity-statement/valid/valid-entity-statement-loose-validation.json',
        'data/person-statement/valid/valid-person-statement.json',
        'data/ownership-or-control-statement/invalid/ownership-or-control-statement-no-statement-type.json',
    ], MissingStatementTypeError),
    ('data/bods-package/fails-secondary-validation/bods-package-missing-entity-statement.json', None,
     UnrecognisedStatementID),
    (
        'data/bods-package/fails-secondary-validation/bods-package-incorrect-ordering.json', None,
        UnrecognisedStatementID),
]


@pytest.mark.parametrize(('json_path', 'json_paths', 'error'), test_invalid_package_json_parametrize_data)
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
    schema_path = 'bods-package.json'
    with open(os.path.join(absolute_path_to_schema_dir, schema_path)) as f:
        schema = json.load(f, object_pairs_hook=OrderedDict)
    with pytest.raises(ValidationError):
        validate(json_data, schema, resolver=resolver, format_checker=format_checker)


test_invalid_statement_json_iter_errors_parametrize_data = [
    ('data/entity-statement/valid/valid-entity-statement.json', set()),
    ('data/entity-statement/valid/valid-entity-statement-loose-validation.json', set()),
    ('data/entity-statement/valid/valid-entity-statement-transliteration-annotations.json', set()),
    ('data/person-statement/valid/valid-person-statement.json', set()),
    ('data/ownership-or-control-statement/valid/valid-ownership-or-control-statement.json', set()),
    ('data/entity-statement/invalid/entity-statement-with-invalid-statement-id.json', {
        "'too-short-so-fail' is too short"
    }),
    ('data/entity-statement/invalid/entity-statement-with-invalid-statement-id-no-entity-type.json', {
        "'too-short-so-fail' is too short",
        "'entityType' is a required property",
    }),
    ('data/entity-statement/invalid/entity-statement-no-publication-details.json', {
        "'publicationDetails' is a required property",
        "Additional properties are not allowed ('publicationDetailsTypo' was unexpected)"
    }),
    ('data/ownership-or-control-statement/invalid/ownership-or-control-statement-no-publication-details.json', {
        "'publicationDetails' is a required property",
        "Additional properties are not allowed ('publicationDetailsTypo' was unexpected)"
    }),
    ('data/person-statement/invalid/person-statement-no-publication-details.json', {
        "'publicationDetails' is a required property",
        "Additional properties are not allowed ('publicationDetailsTypo' was unexpected)"
    }),
    ('data/person-statement/invalid/person-statement-with-invalid-statement-id.json', {
        "'too-short-so-fail' is too short"
    }),
    ('data/person-statement/invalid/person-statement-with-bad-date.json', {
        "'Tuesday' is not a 'date'",
    }),
    ('data/person-statement/invalid/person-statement-no-bods-version.json', {
        "'bodsVersion' is a required property",
        "Additional properties are not allowed ('bodsVersionTypo' was unexpected)"
    }),
    ('data/person-statement/invalid/person-statement-no-publication-date.json', {
        "'publicationDate' is a required property",
        "Additional properties are not allowed ('publicationDateTypo' was unexpected)"
    }),
    ('data/person-statement/invalid/person-statement-no-publisher-sub-prop.json', {
        "OrderedDict([('nameTypo', 'CHRINON LTD')]) is not valid under any of the given schemas",
        "Additional properties are not allowed ('nameTypo' was unexpected)"
    }),
    ('data/person-statement/invalid/person-statement-no-publisher.json', {
        "'publisher' is a required property",
        "Additional properties are not allowed ('publisherTypo' was unexpected)"
    }),
    ('data/person-statement/invalid/person-statement-with-bad-bods-version.json', {
        "'1' does not match '^(\\\\d+\\\\.)(\\\\d+)$'",
    }),
    ('data/person-statement/invalid/person-statement-with-bad-licence-url.json', {
        "'exampledotcom' is not a 'uri'",
    }),
    ('data/person-statement/invalid/person-statement-with-bad-publication-date.json', {
        "'2017/11/18' is not a 'date'",
    }),
    ('data/person-statement/invalid/person-statement-with-bad-publisher-url.json', {
        "'CHRINON LTD' is not a 'uri'",
    }),
    ('data/entity-statement/invalid/entity-statement-invalid-date-in-source.json', {
        "'2018-11-14' is not a 'date-time'",
    }),
    ('data/ownership-or-control-statement/invalid/ownership-or-control-statement-with-invalid-statement-id.json', {
        "'too-short-so-fail' is too short",
    }),
    ('data/ownership-or-control-statement/invalid/ownership-or-control-statement-no-statement-type.json', {
        "'statementType' is a required property",
    }),
]


@pytest.mark.parametrize(('json_path', 'expected_errors'), test_invalid_statement_json_iter_errors_parametrize_data)
def test_invalid_statement_json_iter_errors(json_path, expected_errors):
    with open(os.path.join(this_dir, json_path)) as f:
        json_data = json.load(f, object_pairs_hook=OrderedDict)
    actual_errors = {e.message for e in bods_iter_errors_statement(json_data)}
    assert actual_errors == expected_errors


test_invalid_package_json_iter_errors_parametrize_data = [
    ('data/bods-package/valid/valid-bods-package.json', None, set()),
    ('data/bods-package/valid/valid-bods-package-annotations.json', None, set()),
    ('data/bods-package/valid/valid-bods-package-linking-annotations.json', None, set()),
    (None, [
        'data/entity-statement/valid/valid-entity-statement.json',
        'data/person-statement/valid/valid-person-statement.json',
        'data/ownership-or-control-statement/invalid/ownership-or-control-statement-with-invalid-statement-id.json',
    ], {
        "'too-short-so-fail' is too short"
    }),
    (None, [
        'data/entity-statement/valid/valid-entity-statement.json',
        'data/person-statement/valid/valid-person-statement.json',
        'data/ownership-or-control-statement/invalid/ownership-or-control-statement-no-statement-type.json',
    ], {
        "'statementType' is a required property",
    }),
    (None, [
        'data/entity-statement/invalid/entity-statement-loose-validation-without-required-fields.json',
    ], {
        "OrderedDict([('id', '00335'), ('register', 'Jebel Ali Free Zone')]) is not valid under any of the given schemas",
        "Additional properties are not allowed ('register' was unexpected)"
    }),
    ('data/bods-package/fails-secondary-validation/bods-package-missing-entity-statement.json', None, {
        "subject/describedByEntityStatement '1dc0e987-5c57-4a1c-b3ad-61353b66a9b7' does not match any known entities"
    }),
    ('data/bods-package/fails-secondary-validation/bods-package-missing-interested-party-entity-statement.json', None, {
        "interestedParty/describedByEntityStatement 'd36e6807-020c-4fb5-a0d4-5ab9eb971514' does not match any known entities"
    }),
    ('data/bods-package/fails-secondary-validation/bods-package-incorrect-ordering.json', None, {
        "interestedParty/describedByPersonStatement '019a93f1-e470-42e9-957b-03559861b2e2' does not match any known persons"
    }),
]


@pytest.mark.parametrize(('json_path', 'json_paths', 'expected_errors'), test_invalid_package_json_iter_errors_parametrize_data)
def test_invalid_package_json_iter_errors(json_path, json_paths, expected_errors):
    if json_path:
        with open(os.path.join(this_dir, json_path)) as f:
            json_data = json.load(f, object_pairs_hook=OrderedDict)
    else:
        json_data = [json.load(open(os.path.join(this_dir, json_path)), object_pairs_hook=OrderedDict) for json_path in json_paths]
    actual_errors = {e.message for e in bods_iter_errors_package(json_data)}
    assert actual_errors == expected_errors


def test_all_examples_and_data_files_are_used():
    # Part 1 - get all files we use in tests
    files_used = []
    files_used.extend(test_valid_statement_json_parametrize_data)
    files_used.extend(test_valid_package_json_parametrize_data)
    files_used.extend([a[0] for a in test_invalid_statement_json_parametrize_data])
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
    # Part 2 - get all files we have on disk
    files_we_have = []
    this_dir_len = len(this_dir) if this_dir.endswith('/') else len(this_dir) + 1
    files_we_have.extend([x[this_dir_len:] for x in glob.glob(os.path.join(this_dir, "**", "*.json"), recursive=True)])
    files_we_have.extend([x[this_dir_len:] for x in glob.glob(os.path.join(this_dir, "..", "examples", "**/*.json"), recursive=True)])
    # Part 3 - finally test, make sure all files are used
    files_we_have_but_dont_use = set(files_we_have) - set(files_used)
    assert files_we_have_but_dont_use == set()
