import pytest
import warnings

from jscc.testing.checks import get_empty_files, get_misindented_files


"""
Docs tests

Checks the example data used in the documentation are all valid BODS.
"""


def test_examples_empty(examples_dir):
  """
  Check the data in the /examples directory are not empty
  """
  errors = False
  empties = get_empty_files(top=examples_dir)
  for path in empties:
    warnings.warn(f'ERROR: Empty file at {path}')
    errors = True

  assert not errors, f'Empty files found, see warnings.'


def test_examples_indent(examples_dir):
  """
  Check the data in the /examples directory are indented correctly.
  """
  errors = False
  misindented = get_misindented_files(top=examples_dir)
  for path in misindented:
    warnings.warn(f'ERROR: Misintended files at {path}')
    errors = True

  assert not errors, f'Misindented files found, see warnings.'


def test_examples_valid():
  # check data in /examples directory are valid
  pass


def test_docs():
  # TODO
  # check the docs build
  pass