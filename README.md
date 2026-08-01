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
├── .gitignore
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

Execute os testes automatizados:

```bash
pytest
```

## Funcionalidades

- Leitura de arquivo CSV
- Validação dos dados
- Cálculo da média da turma
- Identificação da maior nota
- Identificação da menor nota
- Contagem de alunos

## Casos de teste implementados

Foram desenvolvidos testes automatizados utilizando pytest para validar diferentes cenários:

- Cálculo correto da média com notas válidas;
- Dataset vazio;
- Ausência da coluna obrigatória "nota";
- Valores de nota inválidos;
- Apenas um aluno no dataset;
- Todas as notas iguais a zero;
- Identificação da maior e menor nota;
- Quantidade de alunos processados;
- Arquivo inexistente;
- Notas negativas;
- Notas acima do limite permitido.

## Melhorias realizadas a partir dos testes

Durante a criação dos testes automatizados foram identificados novos cenários de validação necessários para aumentar a confiabilidade do processamento. Foram adicionadas validações para impedir notas fora do intervalo permitido (0 a 10), além de melhorias no tratamento de erros relacionados à leitura dos arquivos.

Essas alterações demonstram como os testes contribuem para a identificação preventiva de problemas e para a melhoria da qualidade do software.
