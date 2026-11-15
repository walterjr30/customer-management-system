# Customer Management System

[English](README.md) | [Português](README.pt-BR.md)

A command-line Customer Management System developed with **Python, SQLite, and Pytest**.

## About This Project

I developed this project to strengthen my Python programming skills and gain practical experience in software development.

The application allows users to manage customer records through a command-line interface, storing data in a SQLite database.

During development, I practiced CRUD operations, SQL queries, input validation, modular programming, exception handling, automated testing, and refactoring with tests as a safety net.

This project is part of my professional transition into software development.

## Features

- Add new customers
- List registered customers
- Search customers by email
- Update customer city
- Delete customers with confirmation
- Validate and normalize user input
- Prevent duplicate email registrations
- Store data persistently using SQLite
- Run automated tests with Pytest

## Technologies

- **Python**: application logic
- **SQLite**: relational database
- **SQL**: database operations
- **Pytest**: automated testing
- **Ruff**: formatting and linting
- **Git and GitHub**: version control

## Project Structure

```text
customer-management-system/
├── main.py            # menu and user interaction
├── customer.py        # input normalization and validation
├── data_base.py       # SQLite access (db_connection context manager)
├── test/
│   ├── test_customer.py
│   └── test_database.py
├── pyproject.toml     # ruff configuration
├── .gitignore
├── README.md
└── README.pt-BR.md
```

The `customers.db` file is created locally when the application starts.

## Requirements

- Python 3
- Pytest (for running automated tests)
- Ruff (optional, for formatting and linting)

SQLite support is included in Python's standard library.

## Installation and Usage

Clone the repository and navigate to the project directory.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install Pytest (and Ruff, optionally):

```bash
python -m pip install pytest ruff
```

Run the application:

```bash
python main.py
```

The application automatically initializes the SQLite database if it does not already exist.

## Application Menu

```text
--- CUSTOMER MANAGEMENT ---

1 - Add customer
2 - List customers
3 - Search customer
4 - Update customer
5 - Delete customer
0 - Exit
```

## Automated Tests

The test suite covers input validation and normalization, all database operations (including checks that updates and deletes only affect the targeted customer), and the transaction behavior of the `db_connection` context manager (commit, rollback, and connection closing).

Tests use temporary databases, so the real `customers.db` is never touched.

Run the tests:

```bash
python -m pytest -v
```

## Code Quality

Format and lint the code with Ruff:

```bash
ruff format .
ruff check .
```

## What I Learned

- Organizing Python code into modules
- Implementing CRUD operations
- Working with SQLite databases
- Writing parameterized SQL queries
- Handling database errors
- Validating user input
- Creating automated tests with Pytest
- Using temporary databases for testing
- Refactoring safely by writing tests first
- Writing a context manager to centralize commit, rollback, and connection handling
- Verifying tests by deliberately breaking the code
- Using Git with small, descriptive commits
- Formatting and linting with Ruff

## Future Improvements

- Improve email validation (format checking)
- Add tests for the menu functions in `main.py`
- Add type hints and docstrings
- Develop a REST API using FastAPI or Flask
- Implement a graphical or web interface
- Introduce continuous integration with GitHub Actions

## Author

Computer Science graduate and Artificial Intelligence student transitioning into software development, with professional experience in banking operations and administrative management.