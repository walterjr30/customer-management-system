def create_customer(name, email, city):
    email = normalize_email(email)
    customer = {"name": name, "email": email, "city": city}

    return customer


def add_customer(customers, customer):
    customers.append(customer)


def list_customers(customers):
    for customer in customers:
        print("Name: ", customer["name"])
        print("Email: ", customer["email"])
        print("City: ", customer["city"])
        print()


def find_customer(customers, search_email):
    search_email = normalize_email(search_email)
    for customer in customers:
        if customer["email"] == search_email:
            return customer

    return None


def update_customer(customers, email, new_city):
    customer = find_customer(customers, email)

    if customer is not None:
        customer["city"] = new_city
        return True

    return False


def delete_customer(customers, email):
    customer = find_customer(customers, email)
    if customer is not None:
        customers.remove(customer)
        return True

    return False


def normalize_email(email):
    return email.strip().lower()


def normalize_name(name):
    return name.strip()


def normalize_city(city):
    return city.strip()

def is_valid_email_format(email):
    if " " in email or email.count("@") != 1:
        return False
    local, domain = email.split("@")
    if not local or not domain:
        return False
    if "." not in domain.strip("."):
        return False
    return True

def validate_customer(name, email, city):
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
    

def validate_city(city):
    return bool(city.strip())
