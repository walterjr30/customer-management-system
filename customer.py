def normalize_email(email: str) -> str:
    return email.strip().lower()


def normalize_name(name: str) -> str:
    return name.strip()


def normalize_city(city: str) -> str:
    return city.strip()


def is_valid_email_format(email: str) -> bool:
    """
    Return True if the email has one @, text on both sides and a dotted domain.
    """
    if " " in email or email.count("@") != 1:
        return False
    local, domain = email.split("@")
    if not local or not domain:
        return False
    if "." not in domain.strip("."):
        return False
    return True


def validate_customer(name: str, email: str, city: str) -> list[str]:
    """
    Return a list of error messages. An empty list means valid data.
    """
    errors = []
    name = normalize_name(name)
    email = normalize_email(email)
    city = normalize_city(city)

    if not normalize_name(name):
        errors.append("Name is required")
    if not normalize_email(email):
        errors.append("Email is required")
    elif not is_valid_email_format(email):
        errors.append("Email is invalid")
    if not normalize_city(city):
        errors.append("City is required")
    return errors


def validate_city(city: str) -> str:
    """
    return city valid
    """
    return bool(city.strip())
