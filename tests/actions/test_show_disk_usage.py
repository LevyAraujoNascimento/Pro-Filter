from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path


def test_show_disk_usage_file(capsys, tmp_path):
    teste1 = tmp_path / 'test_disk_usage_one.py'
    teste1.touch()
    teste1.write_text('Teste 1')

    teste2 = tmp_path / 'test_disk_usage_two.py'
    teste2.touch()
    teste2.write_text('Teste 2')

    teste3 = tmp_path / 'test_disk_usage_three.py'
    teste3.touch()
    teste3.write_text('Falha')

    context = {
        "all_files": [str(teste1), str(teste2), str(teste3)],
    }

    show_disk_usage(context)
    saida = capsys.readouterr()
    adjustTeste1 = f"'{_get_printable_file_path(str(teste1))}':".ljust(70)
    adjustTeste2 = f"'{_get_printable_file_path(str(teste2))}':".ljust(70)
    adjustTeste3 = f"'{_get_printable_file_path(str(teste3))}':".ljust(70)
    assert (
        saida.out
        == """{} 7 (36%)
{} 7 (36%)
{} 5 (26%)
Total size: 19
""".format(
            adjustTeste1, adjustTeste2, adjustTeste3
        )
    )


def test_show_disk_usage_empty(capsys):
    context = {
        "all_files": [],
    }
    show_disk_usage(context)
    saida = capsys.readouterr()
    assert (
        saida.out
        == """Total size: 0\n"""
    )
