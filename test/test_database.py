import sqlite3
import pytest

from data_base import (
    create_database,
    insert_customer,
    update_customer_city,
    delete_customer_by_email
)

def test_create_database(tmp_path):
    db_path = tmp_path / "test_customer.db"
    create_database(db_path)
    connection = sqlite3.connect(db_path)

    cursor = connection.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name = ?",
        ("customers",)
    )
    result = cursor.fetchone()
    assert result == ("customers",)
    

def test_insert_customer(tmp_path):
    db_path = tmp_path / "test_customers.db"
    create_database(db_path)
    insert_customer("Walter", "walter@email.com", "Dublin", db_path)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM customers WHERE email = ? ",
        ("walter@email.com",)

    )
    customer = cursor.fetchone()
    assert customer[1] == "Walter"
    assert customer[2] == "walter@email.com"
    assert customer[3] == "Dublin"
    
def test_customer_not_found(tmp_path):
    db_path = tmp_path / "test_customer.db"
    create_database(db_path)
    insert_customer("Walter", "walter@email.com", "Dublin", db_path)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM customers WHERE email = ?",
        ("naoexiste@email.com",)

    )

    customer = cursor.fetchone()
    assert customer is None 
    connection.close()

def test_update_customer_city(tmp_path):
    db_path = tmp_path / "test_customer.db"
    create_database(db_path)
    insert_customer("Walter","walter@email.com","Dublin",db_path)
    result = update_customer_city("walter@email.com", "Galway", db_path)

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM customers WHERE email = ?",
        ("walter@email.com",)

    )

    customer = cursor.fetchone()
    assert result is True
    assert customer[3] == "Galway"

    connection.close()

def test_update_customer_not_found(tmp_path):
    db_path = tmp_path / "test_customers.db"
    create_database(db_path)
    result = update_customer_city("naoexiste@email.com", "Cork", db_path)
    assert result is False

def test_delete_customer(tmp_path):
    db_path = tmp_path / "test_customers.db"
    create_database(db_path)
    insert_customer("Walter","walter@email.com","Dublin",db_path)
    result = delete_customer_by_email("walter@email.com", db_path)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM customers WHERE email = ?",
        ("walter@email.com",)
    )
    customer = cursor.fetchone()
    assert result is True
    assert customer is None

    connection.close()

def test_duplicate_email(tmp_path):
    db_path = tmp_path / "test_customer.db"

    create_database(db_path)
    insert_customer(
        "Walter",
        "walter@email.com",
        "Dublin",
        db_path
    )
    with pytest.raises(sqlite3.IntegrityError):
        insert_customer(
            "Maria",
            "walter@email.com",
            "Cork",
            db_path
        )
        
