import pytest

from customer import (
    is_valid_email_format,
    normalize_city,
    normalize_email,
    normalize_name,
    validate_city,
    validate_customer,
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


def test_validate_customer_return_empty_list_when_valid():
    assert validate_customer("Walter", "walter@email.com", "Dublin") == []


@pytest.mark.parametrize(
    "name, email, city, expected_error",
    [
        ("", "teste@email.com", "Brasilia", "Name is required"),
        ("  ", "walter@email.com", "Dublin", "Name is required"),
        ("BBB", "  ", "Maragogi", "Email is required"),
        ("CCC", "ccc@rmail.com", " ", "City is required"),
    ],
)
def test_validate_customer_reports_missing_field(name, email, city, expected_error):
    assert validate_customer(name, email, city) == [expected_error]


@pytest.mark.parametrize(
    "email",
    ["abc", "abc@", "@email.com", "abc@email", "a b@email.com"],
)
def test_validate_customer_reports_invalid_email_format(email):
    assert validate_customer("Walter", email, "Dublin") == ["Email is invalid"]


@pytest.mark.parametrize("email", ["abc@.com", "abc@email."])
def test_is_valid_email_format_rejects_dots_at_domain_edges(email):
    assert is_valid_email_format(email) is False
