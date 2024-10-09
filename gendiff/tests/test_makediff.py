
"""Test makediff module."""

import os

from gendiff.makediff import generate_diff


def get_fixture_path(name):
    """Return path from project root to fixture.

    Args:
        name: fixture name

    Returns:
        Path from project root to fixture
    """
    return os.path.join('gendiff/tests/fixtures', name)


def open_file(path):
    """
    Open file and return it content as string.

    Args:
        path: path tu file

    Returns:
        File content as string
    """
    with open(path, encoding='utf8') as fl:
        return fl.read().strip()


def test_diff_json():
    """Check that json files are compare correctly."""
    filepath1 = get_fixture_path('file1.json')
    filepath2 = get_fixture_path('file2.json')
    correct_diff_path = get_fixture_path('diff_result_json')
    correct = open_file(correct_diff_path)
    diff = generate_diff(filepath1, filepath2)
    assert correct == diff


def test_diff_yaml():
    """Check that yaml files are compare correctly."""
    filepath1 = get_fixture_path('file1.yaml')
    filepath2 = get_fixture_path('file2.yaml')
    correct_diff_path = get_fixture_path('diff_result_yaml')
    correct = open_file(correct_diff_path)
    diff = generate_diff(filepath1, filepath2)
    assert correct == diff
