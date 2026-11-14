import pytest

from customer import (
    normalize_name,
    normalize_city,
    normalize_email,
    create_customer,
    find_customer,
    update_customer,
    delete_customer,
    validate_customer,
    list_customers,
    add_customer,
    validate_city
)
@pytest.fixture
def sample_customers():
    return [
        {"name": "Walter", "email":"walter@email.com","city": "Dublin"},
        {"name": "Maria", "email": "maria@email.com", "city": "Cork"},
        {"name": "John", "email": "jhon@email.com", "city": "Galway"}
        
    ]

@pytest.mark.parametrize(
    "email, expected",
    [
        ("WALTER@EMAIL.COM","walter@email.com"),
        ("  maria@email.com","maria@email.com"),
        ("  JHON@EMAIL.COM","jhon@email.com"),
        ("ana@email.com","ana@email.com")

    ]        
)   

def test_normalize_email(email,expected):
    result = normalize_email(email)
    assert result == expected


 
def test_create_customer():
    result = create_customer("Walter", "WALTER@GMAIL.COM", "Dublin")
    assert result["name"] == "Walter"

def test_find_existing_customer():
    customers = [
        {"name": "Walter", "email": "walter@email.com", "city": "Dublin"},
        {"name": "Maria", "email": "maria@email.com", "city": "Cork"}
    ]
    result = find_customer(customers, "walter@email.com")

    assert result["name"] == "Walter"


def test_find_nonexistent_customer():
    customers = [
            {"name": "Walter", "email": "walter@email.com", "city": "Dublin"},
            {"name": "Maria", "email": "maria@email.com", "city": "Cork"}
    ]   

    result = find_customer(customers, "unknow@email.com")

    assert result is None


def test_update_existing_customer(sample_customers):
    result = update_customer(sample_customers, "walter@email.com", "Galway")

    assert result is True
    assert sample_customers[0]["city"] == "Galway"
    assert sample_customers[1]["city"] == "Cork"

def test_update_nonexistent_customer(sample_customers):
    result = update_customer(sample_customers, "unknown@email.com", "Cork")
    
    assert result is False
    assert sample_customers[0]["city"] == "Dublin"
    assert sample_customers[1]["city"] == "Cork"

def test_delete_existing_customer(sample_customers):
    result = delete_customer(sample_customers, "walter@email.com")
    assert result is True
    assert len(sample_customers) == 2
    assert sample_customers[0]["name"] == "Maria"

def test_delete_nonexistent_customer(sample_customers):
    result = delete_customer(sample_customers, "unknown@email.com")
    assert result is False
    assert len(sample_customers) == 3
    assert sample_customers[0]["name"] == "Walter"
    assert sample_customers[1]["name"] == "Maria"

@pytest.mark.parametrize(
    "name, email, city, expected",
    [
    ("Walter", "walter@email.com", "Dublin", True),
    ("", "maria@email.com", "Cork", False),
    ("John", "john@email.com", "Galway", True),
    ("Heitor", "heitor@email.com", "London", True),
    ("Vanessa", "vanessa@email.com", "Paris", True)
    ]
)

def test_validate_customer(name, email, city, expected):
    result = validate_customer(name,email,city)
    assert result is expected


def test_list_customers(sample_customers,capsys):
    list_customers(sample_customers)
    captured = capsys.readouterr()
    assert "Walter" in captured.out
    assert "Maria" in captured.out
    assert "Dublin" in captured.out
    assert "Cork" in captured.out

def test_add_customer():
    customers = []
    customer = create_customer("Walter", "walter@email.com", "Dublin")
    add_customer(customers, customer)
    assert len(customers) == 1
    assert customers[0]["name"] == "Walter" 

@ pytest.mark.parametrize(
    "city, expected",
    [
        ("Dublin", True),
        (" Galway ", True),
        ("", False),
        ("    ",False)
    ]
        
)
def test_validate_city(city, expected):
    assert validate_city(city) is expected