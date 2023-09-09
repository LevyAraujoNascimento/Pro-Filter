import pytest
from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


def test_find_duplicate_empty(tmp_path):
    teste1 = tmp_path / 'test_one.py'
    teste1.touch()
    teste1.write_text('Teste 1')

    teste2 = tmp_path / 'test_two.py'
    teste2.touch()
    teste2.write_text('Teste 2')

    teste3 = tmp_path / 'test_three.py'
    teste3.touch()
    teste3.write_text('Falha')

    context = {
        "all_files": [str(teste1), str(teste2), str(teste3)],
    }

    result = find_duplicate_files(context)

    assert (
        result
        == []
    )


def test_find_duplicate_files(tmp_path):
    teste1 = tmp_path / 'test_one.py'
    teste1.touch()
    teste1.write_text('Teste')

    teste2 = tmp_path / 'test_two.py'
    teste2.touch()
    teste2.write_text('Teste')

    teste3 = tmp_path / 'test_three.py'
    teste3.touch()
    teste3.write_text('Teste')

    context = {
        "all_files": [str(teste1), str(teste2), str(teste3)],
    }

    result = find_duplicate_files(context)

    assert (
        result
        == [
            (str(teste1), str(teste2)),
            (str(teste1), str(teste3)),
            (str(teste2), str(teste3))
        ]
    )


def test_find_duplicate_undefined_file(tmp_path):
    teste1 = tmp_path / 'test_one.py'
    teste1.touch()
    teste1.write_text('Teste 1')

    context = {
        "all_files": [str(teste1), 'undefined.py'],
    }

    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)
