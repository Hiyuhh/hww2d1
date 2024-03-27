# 1. Real-World Python Dictionary Applications
# Task 1: Restaurant Menu Update
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
restaurant_menu["Beverages"] = {"Soda": 1.99, "Coffee": 2.50}
restaurant_menu["Main Course"].update({"Steak" : 17.99})
restaurant_menu["Starters"].pop("Bruschetta")
print(restaurant_menu)

#2. Advanced Data Handling with Python
# Task 1: Hotel Room Booking Tracker
hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"},
    "103": {"status": "available", "customer": ""}
}

def cli():
    while True:
        user_input = input("""
        Welcome to the Hotel Room Booking Tracker!
        
        Menu:
        1. Book a room
        2. Check out
        3. View rooms
        4. Quit
                        
        """)
                        

        if user_input == "1":
            booking()
        elif user_input == "2":
            check_out()
        elif user_input == "3":
            view_rooms()
        elif user_input == "4":
            break
        else:
            print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")

def booking():
    user_input = input("Which room would you like to book? (Back)")
    if user_input.lower() == "back":
        return
    elif hotel_rooms[user_input]["status"] == "available":
        hotel_rooms[user_input].update({"status" : "booked"})
        print(f"Room {user_input} has been booked")
    elif hotel_rooms[user_input]["status"] == "booked":
        print(f"Room {user_input} is not available")
    else:
        print(f"Room {user_input} does not exist")
    user_input2 = input("What is your name?")
    hotel_rooms[user_input].update({"customer" : user_input2})
    print(f"Room {user_input} has been booked by {user_input2}")
    user_input3 = input("Would you like to book another room? (Yes/No)")
    if user_input3.lower() == "yes":
        booking()
    else:
        return
    
def check_out():
    user_input = input("Which room would you like to check out of? (Back)")
    if user_input.lower() == "back":
        return
    elif hotel_rooms[user_input]["status"] == "booked":
        hotel_rooms[user_input].update({"status" : "available", "customer": ""})
        print(f"Room {user_input} has been Checked out")
    elif hotel_rooms[user_input]["status"] == "available":
        print(f"Room {user_input} is not booked")
    else:
        print(f"Room {user_input} does not exist")
    user_input2 = input("Would you like to check out another room? (Yes/No)")
    if user_input2.lower() == "yes":
        check_out()
    else:
        return

def view_rooms():
    for rooms, details in hotel_rooms.items():
        if details["status"] == "available":
            print(f"Room {rooms} is available")
        elif details["status"] == "booked":
            print(f"Room {rooms} is booked by {details['customer']}")
    input("\nPress enter to go back")
    return

cli()

# Task 2: E-commerce Product Search Feature
products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}
def search():
    products_found = []
    user_input = input("What are you interested in buying? ")
    for product in products.keys():
        if products[product]["name"].casefold() == user_input.casefold():
            products_found.append(product)
    if products_found == []:
        return False
    else:
        return products_found
print(search())

#3. Python Programming Challenges for Customer Service Data Handling
# Task 1: Customer Service Ticket Tracker
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
def cli():
    while True:
        user_input = input("""
        Welcome to the Customer Service Ticket Tracker!
        
        Menu:
        1. Create a ticket
        2. Close a ticket
        3. View tickets
        4. Quit
                        
        """)
                        

        if user_input == "1":
            create_ticket()
        elif user_input == "2":
            close_ticket()
        elif user_input == "3":
            view_tickets()
        elif user_input == "4":
            break
        else:
            print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")

def create_ticket():
    user_input = input("\nWhat is your name?\n")
    user_input2 = input("\nWhat is your issue?\n")
    ticket_number = f"Ticket{len(service_tickets)+1:03}"
    service_tickets[ticket_number] = {"Customer": user_input, "Issue": user_input2, "Status": "open"}
    print(f"{ticket_number} has been created")
    user_input3 = input("\nWould you like to create another ticket? (Yes/No)\n")
    if user_input3.lower() == "yes":
        create_ticket()
    else:
        return

def close_ticket():
    try:
        user_input = input("\nWhich ticket would you like to close? (Back)\n")
        if user_input.lower() == "back":
            return
        elif service_tickets[user_input]["Status"] == "open":
            service_tickets[user_input].update({"Status" : "closed"})
            print(f"{user_input} has been closed")
        elif service_tickets[user_input]["Status"] == "closed":
            print(f"{user_input} is already closed")
    except KeyError:
        print(f"{user_input} does not exist, try again")
        user_input2 = input("\nWould you like to close another ticket? (Yes/No)\n")
        if user_input2.lower() == "yes":
            close_ticket()
        else:
            return

def view_tickets():
    for ticket, details in service_tickets.items():
        print(f"{ticket} is for {details['Customer']}, with a {details['Issue']} and is {details['Status']}")
    input("\nPress enter to go back")
    return

cli()

# 4. Python Essentials for Business Analytics
# Task 1: Sales Data Cloning and Modification
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

import copy
weekly_sales_copy = copy.deepcopy(weekly_sales)
weekly_sales_copy["Week 2"]["Electronics"] = 18000
print(weekly_sales_copy)
print(weekly_sales)