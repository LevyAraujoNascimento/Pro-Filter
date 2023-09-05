import pytest

from pro_filer.actions.main_actions import show_preview  # NOQA


@pytest.fixture
def context():
    return {
      "all_files": ["A", "B", "C", "D", "E", "F"],
      "all_dirs": ["1", "2", "3", "4", "5", "6"],
    }


@pytest.fixture
def empty_context():
    return {
      "all_files": [],
      "all_dirs": []
    }


def test_context(context, capsys):
    show_preview(context)
    assert (
        capsys.readouterr().out
        == """Found 6 files and 6 directories
First 5 files: ['A', 'B', 'C', 'D', 'E']
First 5 directories: ['1', '2', '3', '4', '5']
"""
    )


def test_empty_context(empty_context, capsys):
    show_preview(empty_context)
    assert (
        capsys.readouterr().out
        == """Found 0 files and 0 directories\n"""
    )
