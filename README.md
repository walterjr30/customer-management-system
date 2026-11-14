# Customer Management System

[English](README.md) | [Português](README.pt-BR.md)

A command-line Customer Management System developed with **Python, SQLite, and Pytest**.

## About This Project

I developed this project to strengthen my Python programming skills and gain practical experience in software development.

The application allows users to manage customer records through a command-line interface, storing data in a SQLite database.

During development, I practiced CRUD operations, SQL queries, input validation, modular programming, exception handling, and automated testing.

This project is part of my professional transition into software development.

## Features

- Add new customers
- List registered customers
- Search customers by email
- Update customer city
- Delete customers with confirmation
- Validate user input
- Prevent duplicate email registrations
- Store data persistently using SQLite
- Run automated tests with Pytest

## Technologies

- **Python** — Application logic
- **SQLite** — Relational database
- **SQL** — Database operations
- **Pytest** — Automated testing
- **Git and GitHub** — Version control

## Project Structure

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

The `customers.db` file is created locally when the application starts.

## Requirements

- Python 3
- Pytest (for running automated tests)

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

Install Pytest:

```bash
python -m pip install pytest
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
2 - List customer
3 - Search customer
4 - Update customer
5 - Delete customer
0 - Exit
```

## Automated Tests

The project includes automated tests covering customer management functions, input validation, and SQLite database operations.

Run the tests:

```bash
python -m pytest -v
```

At the latest verified execution, **29 tests passed**.

## What I Learned

- Organizing Python code into modules
- Implementing CRUD operations
- Working with SQLite databases
- Writing parameterized SQL queries
- Handling database errors
- Validating user input
- Creating automated tests with Pytest
- Using temporary databases for testing

## Future Improvements

- Develop a REST API using FastAPI or Flask
- Improve email validation
- Add more integration tests
- Implement a graphical or web interface
- Introduce continuous integration with GitHub Actions

## Author

Computer Science graduate and Artificial Intelligence student transitioning into software development, with professional experience in banking operations and administrative management.