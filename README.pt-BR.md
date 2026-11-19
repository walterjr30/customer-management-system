# Sistema de Gerenciamento de Clientes
![Tests](https://github.com/walterjr30/customer-management-system/actions/workflows/tests.yml/badge.svg)

[English](README.md) | [Português](README.pt-BR.md)

Um Sistema de Gerenciamento de Clientes em linha de comando, desenvolvido com **Python, SQLite e Pytest**.

## Sobre o Projeto

Desenvolvi este projeto para fortalecer minhas habilidades em programação Python e ganhar experiência prática em desenvolvimento de software.

A aplicação permite gerenciar registros de clientes por meio de uma interface de linha de comando, armazenando os dados em um banco de dados SQLite.

Durante o desenvolvimento, pratiquei operações CRUD, consultas SQL, validação de entrada, programação modular, tratamento de exceções, testes automatizados e refatoração com testes como rede de segurança.

Este projeto faz parte da minha transição profissional para o desenvolvimento de software.

## Funcionalidades

- Adicionar novos clientes
- Listar clientes cadastrados
- Buscar clientes por e-mail
- Atualizar a cidade do cliente
- Excluir clientes com confirmação
- Validar e normalizar a entrada do usuário
- Impedir cadastros com e-mail duplicado
- Armazenar dados de forma persistente com SQLite
- Executar testes automatizados com Pytest
- GitHub Actions: automated tests on every push.

## Tecnologias

- **Python**: lógica da aplicação
- **SQLite**: banco de dados relacional
- **SQL**: operações no banco de dados
- **Pytest**: testes automatizados
- **Ruff**: formatação e análise de código
- **Git e GitHub**: controle de versão

## Estrutura do Projeto

```text
customer-management-system/
├── main.py            # menu e interação com o usuário
├── customer.py        # normalização e validação de entrada
├── data_base.py       # acesso ao SQLite (context manager db_connection)
├── test/
│   ├── test_customer.py
│   └── test_database.py
├── pyproject.toml     # configuração do ruff
├── .gitignore
├── README.md
└── README.pt-BR.md
```

O arquivo `customers.db` é criado localmente quando a aplicação é iniciada.

## Requisitos

- Python 3
- Pytest (para executar os testes automatizados)
- Ruff (opcional, para formatação e análise de código)

O suporte ao SQLite já está incluído na biblioteca padrão do Python.

## Instalação e Uso

Clone o repositório e acesse o diretório do projeto.

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative-o no Windows:

```powershell
.venv\Scripts\activate
```

Ative-o no Linux/macOS:

```bash
source .venv/bin/activate
```

Instale o Pytest (e o Ruff, opcionalmente):

```bash
python -m pip install pytest ruff
```

Execute a aplicação:

```bash
python main.py
```

A aplicação inicializa automaticamente o banco de dados SQLite caso ele ainda não exista.

## Menu da Aplicação

```text
--- CUSTOMER MANAGEMENT ---

1 - Add customer
2 - List customers
3 - Search customer
4 - Update customer
5 - Delete customer
0 - Exit
```

O menu da aplicação está em inglês.

## Testes Automatizados

A suíte de testes cobre a validação e a normalização de entrada, todas as operações de banco de dados (incluindo verificações de que atualizações e exclusões afetam apenas o cliente desejado) e o comportamento transacional do context manager `db_connection` (commit, rollback e fechamento da conexão).

Os testes usam bancos de dados temporários, então o `customers.db` real nunca é alterado.

Execute os testes:

```bash
python -m pytest -v
```

## Qualidade de Código

Formate e analise o código com o Ruff:

```bash
ruff format .
ruff check .
```

## O Que Aprendi

- Organizar código Python em módulos
- Implementar operações CRUD
- Trabalhar com bancos de dados SQLite
- Escrever consultas SQL parametrizadas
- Tratar erros de banco de dados
- Validar a entrada do usuário
- Criar testes automatizados com Pytest
- Usar bancos de dados temporários em testes
- Refatorar com segurança escrevendo testes primeiro
- Escrever um context manager para centralizar commit, rollback e gerenciamento da conexão
- Verificar testes quebrando o código de propósito
- Usar Git com commits pequenos e descritivos
- Formatar e analisar código com Ruff

## Melhorias Futuras

- Melhorar a validação de e-mail (verificação de formato)
- Adicionar testes para as funções de menu em `main.py`
- Adicionar type hints e docstrings
- Desenvolver uma API REST com FastAPI ou Flask
- Implementar uma interface gráfica ou web


## Autor

Bacharel em Ciência da Computação e estudante de Inteligência Artificial em transição para o desenvolvimento de software, com experiência profissional em operações bancárias e gestão administrativa.