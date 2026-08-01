import pandas as pd


def carregar_dados(caminho_arquivo):
    """
    Lê um arquivo CSV e retorna um DataFrame.
    """
    try:
        return pd.read_csv(caminho_arquivo)

    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado.")

    except pd.errors.ParserError:
        raise ValueError("Arquivo CSV inválido.")


def validar_dados(df):
    """
    Valida se o DataFrame possui os dados necessários.
    """
    if df.empty:
        raise ValueError("O dataset está vazio.")

    if "aluno" not in df.columns:
        raise KeyError("Coluna 'aluno' não encontrada.")

    if "nota" not in df.columns:
        raise KeyError("Coluna 'nota' não encontrada.")

    try:
        df["nota"] = pd.to_numeric(df["nota"])
    except ValueError:
        raise ValueError("Existem notas inválidas no arquivo.")

    if ((df["nota"] < 0) | (df["nota"] > 10)).any():
        raise ValueError("As notas devem estar entre 0 e 10.")

    return df


def calcular_media(df):
    """
    Calcula a média das notas.
    """
    return df["nota"].mean()


def maior_nota(df):
    return df["nota"].max()


def menor_nota(df):
    return df["nota"].min()


def quantidade_alunos(df):
    return len(df)


def main():
    arquivo = "notas.csv"

    df = carregar_dados(arquivo)
    df = validar_dados(df)

    print(f"Quantidade de alunos: {quantidade_alunos(df)}")
    print(f"Média da turma: {calcular_media(df):.2f}")
    print(f"Maior nota: {maior_nota(df)}")
    print(f"Menor nota: {menor_nota(df)}")


if __name__ == "__main__":
    main()
