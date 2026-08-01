import pandas as pd
import pytest

from script import (
    carregar_dados,
    validar_dados,
    calcular_media,
    maior_nota,
    menor_nota,
    quantidade_alunos
)


def test_calcular_media():
    df = pd.DataFrame({"aluno": ["Ana", "Bruno", "Carlos"], "nota": [8, 7, 9]})
    df = validar_dados(df)
    assert calcular_media(df) == 8


def test_dataset_vazio():
    df = pd.DataFrame(columns=["aluno", "nota"])
    with pytest.raises(ValueError):
        validar_dados(df)


def test_coluna_nota_inexistente():
    df = pd.DataFrame({"aluno": ["Ana", "Bruno"]})
    with pytest.raises(KeyError):
        validar_dados(df)


def test_nota_invalida():
    df = pd.DataFrame({"aluno": ["Ana"], "nota": ["dez"]})
    with pytest.raises(ValueError):
        validar_dados(df)


def test_apenas_um_aluno():
    df = pd.DataFrame({"aluno": ["Ana"], "nota": [10]})
    df = validar_dados(df)
    assert calcular_media(df) == 10
    assert quantidade_alunos(df) == 1
    assert maior_nota(df) == 10
    assert menor_nota(df) == 10


def test_todas_notas_zero():
    df = pd.DataFrame({"aluno": ["Ana", "Bruno"], "nota": [0, 0]})
    df = validar_dados(df)
    assert calcular_media(df) == 0


def test_maior_e_menor_nota():
    df = pd.DataFrame({"aluno": ["Ana", "Bruno"], "nota": [5, 10]})
    df = validar_dados(df)
    assert maior_nota(df) == 10
    assert menor_nota(df) == 5


def test_quantidade_alunos():
    df = pd.DataFrame({"aluno": ["Ana", "Bruno"], "nota": [7, 8]})
    df = validar_dados(df)
    assert quantidade_alunos(df) == 2


def test_nota_negativa():
    df = pd.DataFrame({"aluno": ["Ana"], "nota": [-1]})
    with pytest.raises(ValueError):
        validar_dados(df)


def test_nota_acima_do_limite():
    df = pd.DataFrame({"aluno": ["Ana"], "nota": [11]})
    with pytest.raises(ValueError):
        validar_dados(df)


def test_arquivo_inexistente():
    with pytest.raises(FileNotFoundError):
        carregar_dados("arquivo_inexistente.csv")
