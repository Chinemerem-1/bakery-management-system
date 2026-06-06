"""
Bakery Management System

A Python-based application for recording bakery sales,
tracking revenue, and storing transaction history.

Author: Ogbonna Chinemerem Samuel
Date: June 2026
"""

from datetime import datetime

# Available bakery products and their prices
products = {
    "Bread": 1200,
    "Cake": 5000,
    "Doughnut": 800,
    "Meat Pie": 1500
}

# Calculate sales file and add headers if file is missing or empty
def create_sales_files():
    try:
        with open("sales.txt", "r") as file:
            content = file.read()

        if content.strip() == "":
            with open("sales.txt", "w") as file:
                file.write("Date&Time,Product,Quantity,Revenue\n")

    except FileNotFoundError:
        with open("sales.txt", "w") as file:
            file.write("Date&Time,Product,Quantity,Revenue\n")

# Calculate total revenue from all saved sales records
def load_total_revenue():
    total = 0

    try:
        with open("sales.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(",")

                if parts[0] == "Date&Time":
                    continue

                if len(parts) != 4:
                    continue

                try:
                    revenue = int(parts[3])
                except ValueError:
                    continue

                total += revenue

    except FileNotFoundError:
        pass
    return total

create_sales_files()

def view_products():
    '''Display all available products and their prices'''
    print("\nAvailable Products:")

    for product, price in products.items():
        print(f"{product}: NGN {price}")

def calculate_revenue(price, quantity):
    '''Calculate revenue by multiplying price and quantity'''
    return price * quantity

# Save a sale record with timestamp to sales.txt
def save_file(product_name, quantity, revenue):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("sales.txt", "a") as file:
        file.write(f"{timestamp},{product_name},{quantity},{revenue}\n")

# Record a new sale and validate user input
def record_sale():
    #Ask for product
    product_name = input("\nEnter product sold:")

    if product_name in products:
        try:
            #Ask for quantity
            quantity = int(input("Enter quantity sold: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return

        except ValueError:
            print("Invalid quantity. Please enter a valid number.")
            return
        
        revenue = calculate_revenue(products[product_name], quantity)


        save_file(product_name, quantity, revenue)

        print(f"\nRevenue generated: NGN {revenue}")

        print("Sale saved successfully!")

    else:
        print("Product not found!")

# Display total revenue generated from all sales
def view_total_revenue():
    current_total = load_total_revenue()
    print(f"\nTotal Revenue: NGN {current_total}")

# Sales History Functions
def view_sales_history():
    try:
        with open("sales.txt", "r") as file:

            lines = [line.strip() for line in file if line.strip() != ""]

        if len(lines) == 0:
            print("\nNo sales history found.")
            return

        print("\n===== SALES HISTORY =====")

        for line in lines:

            if line.startswith("Date&Time"):
                continue

            date, product, quantity, revenue = line.split(",")

            print(f"\nDate&Time: {date}")
            print(f"Product:{product}")
            print(f"Quantity: {quantity}")
            print(f"Revenue: NGN {revenue}")
            print("-------------------------------")           

    except FileNotFoundError:
        print("No sales history found.")

# Main menu loop for user interaction
while True:
    print("\n===== BAKERY MANAGEMENT SYSTEM =====")
    print("1. View Products")
    print("2. Record Sale")
    print("3. View Total Revenue")
    print("4. View Sales History")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        view_products()

    elif choice == "2":
        record_sale()

    elif choice == "3":
        view_total_revenue()

    elif choice == "4":
        view_sales_history()

    elif choice == "5":
        print("\nThank you for using the Bakery Management System.")
        break

    else:
        print("Invalid choice. Please try again.")