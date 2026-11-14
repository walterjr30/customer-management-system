# Customer Management System

[English](README.md) · **Português (Brasil)**

Aplicação de terminal em Python para gerenciar cadastros de clientes em um banco de dados SQLite local. Permite cadastrar e listar clientes, buscá-los por e-mail, atualizar a cidade e excluir registros após confirmação.

## Executar a aplicação

Instale o Python com suporte a SQLite. O projeto foi verificado com Python 3.14.7. Na pasta raiz do repositório, execute:

```sh
python main.py
```

A aplicação usa a biblioteca padrão do Python e cria o arquivo `customers.db` na pasta atual na primeira execução.

## Experimentar o menu

1. Escolha **1** para cadastrar um cliente. Informe nome, um e-mail como `demo@example.com` e a cidade. Os três campos são obrigatórios. Use um e-mail em letras minúsculas e sem espaços nas pontas para que as opções de busca, atualização e exclusão encontrem o cadastro.
2. Escolha **2** para listar os clientes ou **3** para buscar um cliente por e-mail.
3. Escolha **4** para atualizar a cidade de um cliente.
4. Escolha **5** para excluir um cliente. Digite **Y** para confirmar ou **N** para cancelar.
5. Escolha **0** para sair.

## Executar os testes

O Pytest é necessário apenas para os testes. Crie um ambiente virtual e use diretamente o executável do Python desse ambiente.

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install pytest==9.2.0
.\.venv\Scripts\python.exe -m pytest -q
```

**macOS ou Linux**

```sh
python3 -m venv .venv
.venv/bin/python -m pip install pytest==9.2.0
.venv/bin/python -m pytest -q
```

Os 29 testes exercitam as funções auxiliares de cadastro e as operações SQLite. Os testes de banco de dados usam arquivos temporários.

## Estrutura do projeto

| Caminho | Finalidade |
| --- | --- |
| `main.py` | Menu interativo e ponto de entrada da aplicação |
| `customer.py` | Funções auxiliares, normalização e verificação de campos obrigatórios |
| `data_base.py` | Estrutura do banco SQLite e operações de persistência |
| `test/` | Testes das funções auxiliares e do banco de dados com Pytest |
