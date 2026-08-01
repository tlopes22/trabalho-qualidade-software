import pandas as pd
import pytest

from script import (
    validar_dados,
    calcular_media,
    maior_nota,
    menor_nota,
    quantidade_alunos
)


def test_calcular_media():
    """
    Testa se a média é calculada corretamente.
    """
    df = pd.DataFrame({
        "aluno": ["Ana", "Bruno", "Carlos"],
        "nota": [8, 7, 9]
    })

    df = validar_dados(df)

    assert calcular_media(df) == 8


def test_dataset_vazio():
    """
    Deve lançar erro quando o DataFrame estiver vazio.
    """
    df = pd.DataFrame(columns=["aluno", "nota"])

    with pytest.raises(ValueError):
        validar_dados(df)


def test_coluna_nota_inexistente():
    """
    Deve lançar erro caso a coluna 'nota' não exista.
    """
    df = pd.DataFrame({
        "aluno": ["Ana", "Bruno"]
    })

    with pytest.raises(KeyError):
        validar_dados(df)


def test_nota_invalida():
    """
    Deve lançar erro quando houver nota não numérica.
    """
    df = pd.DataFrame({
        "aluno": ["Ana", "Bruno"],
        "nota": ["dez", 8]
    })

    with pytest.raises(ValueError):
        validar_dados(df)


def test_apenas_um_aluno():
    """
    Testa cálculo da média com apenas um aluno.
    """
    df = pd.DataFrame({
        "aluno": ["Ana"],
        "nota": [10]
    })

    df = validar_dados(df)

    assert calcular_media(df) == 10
    assert quantidade_alunos(df) == 1
    assert maior_nota(df) == 10
    assert menor_nota(df) == 10


def test_todas_notas_zero():
    """
    Testa cenário em que todas as notas são zero.
    """
    df = pd.DataFrame({
        "aluno": ["Ana", "Bruno", "Carlos"],
        "nota": [0, 0, 0]
    })

    df = validar_dados(df)

    assert calcular_media(df) == 0
    assert maior_nota(df) == 0
    assert menor_nota(df) == 0


def test_maior_e_menor_nota():
    """
    Verifica maior e menor nota da turma.
    """
    df = pd.DataFrame({
        "aluno": ["Ana", "Bruno", "Carlos"],
        "nota": [5, 10, 8]
    })

    df = validar_dados(df)

    assert maior_nota(df) == 10
    assert menor_nota(df) == 5


def test_quantidade_alunos():
    """
    Verifica a quantidade de alunos.
    """
    df = pd.DataFrame({
        "aluno": ["Ana", "Bruno", "Carlos", "Daniel"],
        "nota": [7, 8, 9, 10]
    })

    df = validar_dados(df)

    assert quantidade_alunos(df) == 4
