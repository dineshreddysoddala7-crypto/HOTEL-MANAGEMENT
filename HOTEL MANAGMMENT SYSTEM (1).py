from datetime import datetime

rooms = {
    101: {"status": "Available", "price": 2000, "type": "Double"},
    102: {"status": "Available", "price": 2000, "type": "Double"},
    103: {"status": "Available", "price": 1500, "type": "Triple"},
    104: {"status": "Available", "price": 1500, "type": "Triple"},
    105: {"status": "Available", "price": 1500, "type": "Triple"}
}

customers = {}

def view_rooms():
    print("\nRoom Status:")
    for room, details in rooms.items():
        print(f"Room {room}: {details['status']} | {details['type']} | ₹{details['price']}/day")

def book_room():
    room_no = int(input("Enter room number to book: "))
    
    if room_no in rooms and rooms[room_no]["status"] == "Available":
        name = input("Enter customer name: ")
        
        # Mobile validation
        while True:
            mobile = input("Enter 10-digit mobile number: ")
            if mobile.isdigit() and len(mobile) == 10:
                break
            else:
                print("Invalid number! Enter exactly 10 digits.")
        
        # Date input
        checkin = input("Enter check-in date (DD-MM-YYYY): ")
        checkout = input("Enter check-out date (DD-MM-YYYY): ")
        
        try:
            checkin_date = datetime.strptime(checkin, "%d-%m-%Y")
            checkout_date = datetime.strptime(checkout, "%d-%m-%Y")
        except:
            print("Invalid date format!")
            return
        
        # Calculate days
        days = (checkout_date - checkin_date).days
        
        if days <= 0:
            print("Invalid dates! Checkout must be after check-in.")
            return
        
        price_per_day = rooms[room_no]["price"]
        total_bill = price_per_day * days
        
        rooms[room_no]["status"] = "Booked"
        customers[room_no] = {
            "name": name,
            "mobile": mobile,
            "days": days,
            "bill": total_bill,
            "type": rooms[room_no]["type"],
            "checkin": checkin,
            "checkout": checkout
        }
        
        print("\nRoom booked successfully!")
        print(f"Stay Duration: {days} days")
        print(f"Total cost = ₹{total_bill}")
    else:
        print("Room not available!")

def checkout():
    room_no = int(input("Enter room number for checkout: "))
    
    if room_no in customers:
        customer = customers[room_no]
        
        print("\n--- BILL DETAILS ---")
        print(f"Name: {customer['name']}")
        print(f"Mobile: {customer['mobile']}")
        print(f"Room Type: {customer['type']}")
        print(f"Check-in Date: {customer['checkin']}")
        print(f"Check-out Date: {customer['checkout']}")
        print(f"Days Stayed: {customer['days']}")
        print(f"Total Amount: ₹{customer['bill']}")
        
        print("\nCheckout successful!")
        
        rooms[room_no]["status"] = "Available"
        del customers[room_no]
    else:
        print("Invalid room or already empty!")

def view_customers():
    print("\nCustomer Details:")
    
    if not customers:
        print("No customers currently.")
    else:
        for room, details in customers.items():
            print(f"Room {room}: {details['name']} ({details['type']}, {details['days']} days)")

while True:
    print("\n--- Hotel Management System ---")
    print("1. View Rooms")
    print("2. Book Room")
    print("3. Checkout")
    print("4. View Customers")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Please enter a valid number!")
        continue

    if choice == 1:
        view_rooms()
    elif choice == 2:
        book_room()
    elif choice == 3:
        checkout()
    elif choice == 4:
        view_customers()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")