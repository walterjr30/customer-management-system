import pytest

from customer import (
    normalize_name,
    normalize_city,
    normalize_email,
    validate_customer,
    validate_city,
)


@pytest.mark.parametrize(
    "email, expected",
    [
        ("WALTER@EMAIL.COM", "walter@email.com"),
        ("  maria@email.com", "maria@email.com"),
        ("  JHON@EMAIL.COM", "jhon@email.com"),
        ("ana@email.com", "ana@email.com"),
    ],
)
def test_normalize_email(email, expected):
    result = normalize_email(email)
    assert result == expected


@pytest.mark.parametrize(
    "name, expected",
    [
        (" Walter ", "Walter"),
        ("Walter", "Walter"),
        ("Ana Maria", "Ana Maria"),
        ("  ", ""),
    ],
)
def test_normalize_name(name, expected):
    result = normalize_name(name)
    assert result == expected


@pytest.mark.parametrize(
    "city, expected",
    [
        (" Dublin ", "Dublin"),
        ("Dublin", "Dublin"),
        ("  ", ""),
    ],
)
def test_normalize_city(city, expected):
    result = normalize_city(city)
    assert result == expected


@pytest.mark.parametrize(
    "city, expected",
    [("Dublin", True), (" Galway ", True), ("", False), ("    ", False)],
)
def test_validate_city(city, expected):
    assert validate_city(city) is expected


@pytest.mark.parametrize(
    "name, email, city",
    [
        ("", "semnome@email.com", "uberlandia"),
        ("Sememail", "", "Belo Horizonte"),
        ("Sem cidade", "semcidade@email.com", ""),
        ("    ", "ana@email.com", "Analandia"),
    ],
)
def test_validate_customer_rejects_invalid(name, email, city):
    assert validate_customer(name, email, city) is False


def test_validate_customer_accepts_valid():
    assert validate_customer("Walter", "walter@email.com", "Dublin") is True
