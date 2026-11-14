# Sistema de Gerenciamento de Clientes

[English](README.md) | [Português](README.pt-BR.md)

Sistema de gerenciamento de clientes desenvolvido em **Python, SQLite e Pytest**, com interface de linha de comando.

## Sobre o Projeto

Desenvolvi este projeto para aprimorar meus conhecimentos em Python e adquirir experiência prática em desenvolvimento de software.

A aplicação permite gerenciar cadastros de clientes por meio de um menu interativo, armazenando as informações em um banco de dados SQLite.

Durante o desenvolvimento, pratiquei operações CRUD, consultas SQL, validação de dados, programação modular, tratamento de exceções e testes automatizados.

Este projeto faz parte da minha transição profissional para a área de desenvolvimento de software.

## Funcionalidades

- Cadastrar novos clientes
- Listar clientes cadastrados
- Buscar clientes pelo e-mail
- Atualizar a cidade de um cliente
- Excluir clientes mediante confirmação
- Validar os dados informados
- Impedir cadastros com e-mails duplicados
- Armazenar os dados permanentemente com SQLite
- Executar testes automatizados com Pytest

## Tecnologias Utilizadas

- **Python** — Lógica da aplicação
- **SQLite** — Banco de dados relacional
- **SQL** — Operações no banco de dados
- **Pytest** — Testes automatizados
- **Git e GitHub** — Controle de versão

## Estrutura do Projeto

```text
customer-management-system/
├── main.py
├── customer.py
├── data_base.py
├── test/
│   ├── test_customer.py
│   └── test_database.py
├── .gitignore
├── README.md
└── README.pt-BR.md
```

O arquivo `customers.db` é criado localmente quando a aplicação é iniciada.

## Requisitos

- Python 3
- Pytest (para executar os testes automatizados)

O suporte ao SQLite já faz parte da biblioteca padrão do Python.

## Instalação e Execução

Clone o repositório e acesse a pasta do projeto.

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente no Windows:

```powershell
.venv\Scripts\activate
```

Instale o Pytest:

```bash
python -m pip install pytest
```

Execute o programa:

```bash
python main.py
```

A aplicação inicializa automaticamente o banco de dados SQLite, caso ele ainda não exista.

## Menu da Aplicação

```text
--- CUSTOMER MANAGEMENT ---

1 - Add customer
2 - List customer
3 - Search customer
4 - Update customer
5 - Delete customer
0 - Exit
```

## Testes Automatizados

O projeto possui testes automatizados para verificar as funções de gerenciamento de clientes, validação de dados e operações no banco SQLite.

Para executar os testes:

```bash
python -m pytest -v
```

Na última execução verificada, **29 testes passaram**.

## Conhecimentos Desenvolvidos

- Organização de código Python em módulos
- Implementação de operações CRUD
- Integração com banco de dados SQLite
- Utilização de consultas SQL parametrizadas
- Tratamento de erros no banco de dados
- Validação de entradas do usuário
- Desenvolvimento de testes automatizados com Pytest
- Utilização de bancos de dados temporários nos testes

## Melhorias Futuras

- Desenvolver uma API REST com FastAPI ou Flask
- Aprimorar a validação de e-mails
- Adicionar mais testes de integração
- Criar uma interface gráfica ou web
- Implementar integração contínua com GitHub Actions

## Autor

Graduado em Ciência da Computação e estudante de Inteligência Artificial, em transição profissional para desenvolvimento de software, com experiência anterior em operações bancárias e gestão administrativa.