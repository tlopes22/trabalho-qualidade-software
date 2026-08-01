# Trabalho Prático - Qualidade de Software

## Objetivo

Desenvolver um script em Python responsável por processar um conjunto de dados contendo alunos e notas, aplicando testes automatizados para garantir a qualidade do software.

## Tecnologias utilizadas

- Python 3.x
- Pandas
- Pytest

## Estrutura do projeto

```
Trabalho-QualidadeSoftware/

├── script.py
├── test_script.py
├── notas.csv
├── requirements.txt
├── README.md
└── relatorio.pdf
```

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o programa:

```bash
python script.py
```

Execute os testes:

```bash
pytest
```

## Funcionalidades

- Leitura de arquivo CSV
- Validação dos dados
- Cálculo da média da turma
- Maior nota
- Menor nota
- Quantidade de alunos

## Casos de teste

Foram implementados testes para:

- Média correta
- Dataset vazio
- Coluna "nota" inexistente
- Nota inválida
- Apenas um aluno
- Todas as notas iguais a zero
- Maior e menor nota
- Quantidade de alunos
