from datetime import date

from pro_filer.actions.main_actions import show_details  # NOQA


data = date.today()


def test_show_details_file(capsys, tmp_path):
    arq = tmp_path / 'teste.py'
    with open(arq, "w", encoding="utf-8") as file:
        file.write('teste')
    context = {
        "base_path": str(arq),
    }
    show_details(context)
    saida = capsys.readouterr()
    assert (
        saida.out
        == """File name: teste.py
File size in bytes: 5
File type: file
File extension: .py
Last modified date: {}
""".format(
            data
        )
    )


def test_show_details_dic(capsys, tmp_path):
    dic = tmp_path / 'src'
    dic.touch()
    context = {
        "base_path": str(dic),
    }
    show_details(context)
    saida = capsys.readouterr()
    assert (
        saida.out
        == """File name: src
File size in bytes: 0
File type: file
File extension: [no extension]
Last modified date: {}
""".format(
            data
        )
    )


def test_show_details_wrong(capsys):
    context = {
        "base_path": 'ERRO',
    }
    show_details(context)
    saida = capsys.readouterr()
    assert (
        saida.out == """File 'ERRO' does not exist\n"""
    )
