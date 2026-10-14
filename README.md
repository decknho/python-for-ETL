# Python for ETL

Projeto prático de desenvolvimento de pipelines **ETL (Extract, Transform, Load)** utilizando Python, com foco na extração, transformação e carga de dados em um banco de dados SQL.

## 🎯 Objetivo

Construir um pipeline ETL modular, capaz de processar diferentes conjuntos de dados, realizar transformações e preparar informações para armazenamento estruturado em um banco de dados relacional.

O projeto também tem como objetivo praticar organização de código, modularização e boas práticas de desenvolvimento de pipelines de dados.

## 🛠️ Tecnologias

- **Python:** desenvolvimento dos processos ETL.
- **Jupyter Notebook:** experimentação e documentação dos testes.
- **SQL:** armazenamento e consulta dos dados.
- **Git e GitHub:** versionamento e documentação do projeto.

## 📁 Estrutura do projeto

```text
python-for-ETL/
├── data/
│   ├── products/
│   └── users/
├── ETL/
│   ├── extract.py
│   └── transform.py
├── main.ipynb
├── .gitignore
├── LICENSE
└── README.md
```

## 🔄 Pipeline ETL

O projeto será organizado em três etapas:

### 1. Extract — Extração

Responsável por obter os dados de suas fontes e disponibilizá-los para processamento.

### 2. Transform — Transformação

Responsável pelo tratamento e pela preparação dos dados, incluindo limpeza, padronização, validação e adequação às estruturas de destino.

### 3. Load — Carga

Etapa planejada para inserir os dados transformados em tabelas de um banco de dados SQL, respeitando a estrutura e os requisitos de cada conjunto de dados.

## 🗂️ Organização dos dados

Os diretórios `data/users/` e `data/products/` serão utilizados para organizar os arquivos relacionados a cada domínio.

A proposta é trabalhar com diferentes conjuntos de dados e preparar cada um para sua respectiva tabela no banco de dados, mantendo o código organizado e facilitando a manutenção do pipeline.

## 🚧 Status

Em desenvolvimento.

Atualmente, o projeto está concentrado nas etapas de extração e transformação. A etapa de carga será implementada após a conclusão e validação das transformações.

## 📚 Objetivos de aprendizado

- Desenvolver pipelines ETL com Python.
- Trabalhar com diferentes conjuntos de dados.
- Aplicar técnicas de limpeza, transformação e validação de dados.
- Integrar Python a um banco de dados SQL.
- Organizar processos de dados de maneira modular e reutilizável.

---

Projeto desenvolvido para fins de estudo e construção de portfólio em dados.
