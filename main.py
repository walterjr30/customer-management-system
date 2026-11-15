import sqlite3

from customer import(
    validate_customer,
    validate_city,
    normalize_email
)

from data_base import(
    find_customer_by_email,
    create_database,
    insert_customer,
    get_customers,
    update_customer_city,
    delete_customer_by_email
)



def show_menu():
    print("\n --- CUSTOMER MANAGEMENT ---")
    print("1 - Add customer")
    print("2 - List customers")
    print("3 - Search customer")
    print("4 - Update customer")
    print("5 - Delete customer")
    print("0 - Exit")
    

def print_customer(customer):
    print(f"Name:  {customer['name']}")
    print(f"Email: {customer['email']}")
    print(f"City:  {customer['city']}")
    print()

def list_customers():
    customers = get_customers()

    if not customers:
        print("No customer found")
        return

    for customer in customers:
        print_customer(customer)
    print("Total customers:", len(customers))

def search_customer():
    email_verify = normalize_email(input("Input email for verification: "))
    customer = find_customer_by_email(email_verify)
    if customer is None:
        print("Customer not found")
        return
    
    print("Customer found")
    print_customer(customer)

create_database()

while True:
    show_menu()
    option = input("Choose your option: ")
    if option == "1":
        name = input("Enter name: ").strip()
        email = normalize_email(input("Enter email: "))
        city = input("Enter city: ").strip()
        validate = validate_customer(name, email, city)
        if validate:
            verify_customer = find_customer_by_email(email)
            if verify_customer is not None:
                print("Email already registered")
            else:
                try:
                    insert_customer(name, email, city)
                    print("Customer added successfully")
                except sqlite3.IntegrityError:
                    print("Email already registered")       
        else:
            print("All fields are required")        
    
    elif option == "2":
       list_customers()    

    elif option == "3":
        search_customer()

    elif option == "4":
        email_update = normalize_email(input("Input email for update: "))
        city_update = input("Enter new city for update: ").strip()
        validation_city = validate_city(city_update)
        if validation_city:
            updated = update_customer_city(email_update, city_update)
            if updated:
                print("Customer updated successfully!")
            else:
                print("Customer not found")
        else:
            print("City cannot be empty")    

    elif option == "5":
        email_to_delete = normalize_email(input("Enter email for delete: "))
        customer = find_customer_by_email(email_to_delete)
        if customer is not None:
            question = input("Are you sure you want to delete this customer? (Y/N)").strip().upper()
            if question == "Y":
                deleted = delete_customer_by_email(email_to_delete)
                if deleted:
                    print("Customer deleted successfully")
                else:
                    print("Customer could not be deleted")    
            elif question == "N":
                print("Deletion cancelled")
            else:
                print("Invalid option")    
        else:
            print("Customer not found")
        


    elif option == "0":
        break
    else:
        print("Invalid option")

