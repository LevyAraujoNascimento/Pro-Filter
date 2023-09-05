import pytest

from pro_filer.actions.main_actions import show_preview  # NOQA


@pytest.fixture
def context():
    return {
      "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
      "all_dirs": ["src", "src/utils"]
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
        == """Found 3 files and 2 directories
First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']
First 5 directories: ['src', 'src/utils']
"""
    )


def test_empty_context(empty_context, capsys):
    show_preview(empty_context)
    assert (
        capsys.readouterr().out
        == """Found 0 files and 0 directories\n"""
    )
