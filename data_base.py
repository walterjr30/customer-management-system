import sqlite3
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
    connection = get_connection(db_path)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            city TEXT NOT NULL
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()


def insert_customer(name, email, city, db_path=DB_PATH):
    connection = get_connection(db_path)
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO customers (name, email, city) VALUES (?,?,?)",
            (name, email, city),
        )
        connection.commit()
        cursor.close()

    finally:
        connection.close()


def get_customers(db_path=DB_PATH):
    connection = get_connection(db_path)

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customers")

        customers = cursor.fetchall()

        return customers

    finally:
        connection.close()


def find_customer_by_email(email, db_path=DB_PATH):
    connection = get_connection(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customers WHERE email=?", (email,))
    customer = cursor.fetchone()

    cursor.close()
    connection.close()
    return customer


def update_customer_city(email, new_city, db_path=DB_PATH):
    connection = get_connection(db_path)
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE customers SET city = ? WHERE email = ?", (new_city, email)
            )
            result = cursor.rowcount

        return result > 0

    finally:
        connection.close()


def delete_customer_by_email(email, db_path=DB_PATH):
    connection = get_connection(db_path)
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM customers WHERE email = ?", (email,))
            result = cursor.rowcount
        return result > 0

    finally:
        connection.close()
