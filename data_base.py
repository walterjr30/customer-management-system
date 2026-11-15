import sqlite3
import pytest
from contextlib import contextmanager

DB_PATH = "customers.db"

@contextmanager
def db_connection(db_path=DB_PATH):
    connection = get_connection(db_path)
    try:
        with connection:
            yield connection
    finally:
        connection.close()



def get_connection(db_path=DB_PATH):
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


def create_database(db_path=DB_PATH):
    with db_connection(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                city TEXT NOT NULL
            )
        """
        )

    


def insert_customer(name, email, city, db_path=DB_PATH):
    with db_connection(db_path) as conn:
        conn.execute(
            "INSERT INTO customers (name, email, city) VALUES (?,?,?)",
            (name, email, city),
        )
        


def get_customers(db_path=DB_PATH):
    with db_connection(db_path) as conn:
        return conn.execute(
            "SELECT * FROM customers ORDER BY name"
            ).fetchall()
        

def find_customer_by_email(email, db_path=DB_PATH):
    with db_connection(db_path) as conn:
        return conn.execute(
            "SELECT * FROM customers WHERE email=?", (email,)
        ).fetchone()
    

def update_customer_city(email, new_city, db_path=DB_PATH):
    with db_connection(db_path) as conn:
        cursor = conn.execute(
            "UPDATE customers SET city = ? WHERE email = ?",
            (new_city, email),
            )
        return cursor.rowcount > 0
            


def delete_customer_by_email(email, db_path=DB_PATH):
    with db_connection(db_path) as conn:
        cursor = conn.execute(
            "DELETE FROM customers WHERE email = ?",
            (email,)
        )
        return cursor.rowcount > 0

def test_db_connection_closes_connection_on_error(db_path):
    saved = None

    with pytest.raises(ValueError):
        with db_connection(db_path) as conn:
            saved = conn
            raise ValueError("boom")

    with pytest.raises(sqlite3.ProgrammingError):
        saved.execute("SELECT 1")

def test_db_connection_rolls_back_on_error(db_path):
    with pytest.raises(ValueError):
        with db_connection(db_path) as conn:
            conn.execute(
                "INSERT INTO customers (name, email, city) VALUES (?,?,?)",
                ("Walter", "walter@email.com", "Dublin"),
            )
            raise ValueError("boom")

    assert get_customers(db_path) == []