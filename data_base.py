import sqlite3
from contextlib import contextmanager
from pathlib import Path
from collections.abc import Iterator


DB_PATH = "customers.db"
DbPath = str | Path


@contextmanager
def db_connection(db_path: DbPath = DB_PATH) -> Iterator[sqlite3.Connection]:
    connection = get_connection(db_path)
    try:
        with connection:
            yield connection
    finally:
        connection.close()


def get_connection(db_path: DbPath = DB_PATH) -> sqlite3.Connection:
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


def create_database(db_path: DbPath = DB_PATH) -> None:
    with db_connection(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                city TEXT NOT NULL
            )
        """)


def insert_customer(
    name: str, email: str, city: str, db_path: DbPath = DB_PATH
) -> None:
    with db_connection(db_path) as conn:
        conn.execute(
            "INSERT INTO customers (name, email, city) VALUES (?,?,?)",
            (name, email, city),
        )


def get_customers(db_path: DbPath = DB_PATH) -> list[sqlite3.Row]:
    with db_connection(db_path) as conn:
        return conn.execute("SELECT * FROM customers ORDER BY name").fetchall()


def find_customer_by_email(email: str, db_path: DbPath = DB_PATH) -> sqlite3.Row | None:
    with db_connection(db_path) as conn:
        return conn.execute(
            "SELECT * FROM customers WHERE email=?", (email,)
        ).fetchone()


def update_customer_city(email: str, new_city: str, db_path: DbPath = DB_PATH) -> bool:
    with db_connection(db_path) as conn:
        cursor = conn.execute(
            "UPDATE customers SET city = ? WHERE email = ?",
            (new_city, email),
        )
        return cursor.rowcount > 0


def delete_customer_by_email(email: str, db_path: DbPath = DB_PATH) -> bool:
    with db_connection(db_path) as conn:
        cursor = conn.execute("DELETE FROM customers WHERE email = ?", (email,))
        return cursor.rowcount > 0
