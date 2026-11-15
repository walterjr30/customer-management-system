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

def update_customer():
    email_update = normalize_email(input("Input email for update: "))
    new_city = input("Enter new city for update: ").strip()
    if not validate_city(new_city):
        print("City cannot be empty")  
        return
    if not update_customer_city(email_update, new_city):
        print("Customer not found")
        return
    
    print("Customer updated successfully!")
        
def delete_customer():
    email_to_delete = normalize_email(input("Enter email for delete: "))
    customer = find_customer_by_email(email_to_delete)
    if customer is None:
        print("Customer not found")
        return
    question = input("Are you sure you want to delete this customer? (Y/N): ").strip().upper()
    if question == "N":
        print("Deletion cancelled")
        return
    if question != "Y":
        print("Invalid option")
        return
    
    deleted = delete_customer_by_email(email_to_delete)
    if deleted:
        print("Customer deleted successfully")
    else:
        print("Customer could not be deleted")    
        
def add_customer():
    name = input("Enter name: ").strip()
    email = normalize_email(input("Enter email: "))
    city = input("Enter city: ").strip()
    if not validate_customer(name, email, city):
        print("All fields are required") 
        return
    if find_customer_by_email(email) is not None:
        print("Email already registered")
        return
    try:
        insert_customer(name, email, city)
        print("Customer added successfully")
    except sqlite3.IntegrityError:
        print("Email already registered")


create_database()
    
while True:
    show_menu()
    option = input("Choose your option: ")
    if option == "1":
       add_customer() 
    elif option == "2":
       list_customers()    
    elif option == "3":
        search_customer()
    elif option == "4":
        update_customer()      
    elif option == "5":
        delete_customer()
    elif option == "0":
        break
    else:
        print("Invalid option")

