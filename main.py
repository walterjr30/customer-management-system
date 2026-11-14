import sqlite3

from customer import(
    create_customer,
    add_customer,   
    list_customers,
    find_customer,
    update_customer,
    delete_customer,
    validate_customer,
    
)

from data_base import(
    find_customer_by_email,
    create_database,
    insert_customer,
    get_customers,
    update_customer_city,
    delete_customer_by_email
)

create_database()
clients = []
while True:
    print("\n --- CUSTOMER MANAGEMENT ---")
    print("1 - Add customer")
    print("2 - List customer")
    print("3 - Search customer")
    print("4 - Update customer")
    print("5 - Delete customer")
    print("0 - Exit")

    option = input("Choose your option: ")

    if option == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        city = input("Enter city: ")
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
        customers = get_customers()
        i = 0
        if customers:
            for customer in customers:
                print("Name: ", customer[1])
                print("Email: ", customer[2])
                print("City: ", customer[3])
            print("Total customers:", len(customers))
        else:
            print("No customer found")    

    elif option == "3":
        email_verify = input("Input email for verification: ").strip().lower()
        customer = find_customer_by_email(email_verify)
        if customer is not None:
            print("Customer found ")
            print("Name: ", customer[1])
            print("Email: ", customer[2])
            print("City: ", customer[3]) 
        else:
            print("Customer not found")

    elif option == "4":
        email_update = input("Input email for update: ").strip().lower()
        city_update = input("Enter new city for update: ").strip()
        updated = update_customer_city(email_update, city_update)
        if updated:
            print("Customer updated successfully!")
        else:
            print("Customer not found")    

    elif option == "5":
        email_deleted = input("Enter email for delete: ").strip().lower()
        customer = find_customer_by_email(email_deleted)
        if customer is not None:
            question = input("Are you sure you want to delete this customer? (Y/N)").strip().upper()
            if question == "Y":
                email_deleted = delete_customer_by_email(email_deleted)
                if email_deleted:
                    print("Customer deleted successfully")
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

