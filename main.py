import random
import json

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = random.randint(1000, 9999)
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = food_id
        self.food_items.append(food_item)
        print("Food item added successfully.")

    def edit_food_item(self, food_id, new_details):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                for key, value in new_details.items():
                    setattr(food_item, key, value)
                print("Food item updated successfully.")
                return
        print("Food item not found.")

    def view_food_items(self):
        if len(self.food_items) == 0:
            print("No food items available.")
        else:
            print("Food Items:")
            for food_item in self.food_items:
                print(f"Food ID: {food_item.food_id}")
                print(f"Name: {food_item.name}")
                print(f"Quantity: {food_item.quantity}")
                print(f"Price: {food_item.price}")
                print(f"Discount: {food_item.discount}")
                print(f"Stock: {food_item.stock}")
                print()

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully.")
                return
        print("Food item not found.")

class User:
    def __init__(self):
        self.orders = []

    def register(self, full_name, phone_number, email, address, password):
        # Implement user registration logic here
        print("User registered successfully.")

    def login(self, email, password):
        # Implement user login logic here
        print("User logged in successfully.")

    def place_new_order(self):
        # Show the list of food items and allow the user to select items to order
        if len(admin.food_items) == 0:
            print("No food items available for ordering.")
        else:
            print("Food Items:")
            for food_item in admin.food_items:
                print(f"{food_item.name} ({food_item.quantity}) [INR {food_item.price}]")
            selected_items = input("Enter the numbers of the items you want to order (comma-separated): ")
            selected_item_numbers = [int(num) for num in selected_items.split(",")]
            ordered_items = []
            for number in selected_item_numbers:
                if number >= 1 and number <= len(admin.food_items):
                    ordered_items.append(admin.food_items[number-1])
            if len(ordered_items) == 0:
                print("No valid items selected for ordering.")
            else:
                print("Selected Items:")
                for item in ordered_items:
                    print(f"{item.name} ({item.quantity}) [INR {item.price}]")
                place_order = input("Do you want to place the order? (yes/no): ")
                if place_order.lower() == "yes":
                    self.orders.append(ordered_items)
                    print("Order placed successfully.")
                else:
                    print("Order canceled.")

    def order_history(self):
        if len(self.orders) == 0:
            print("No order history found.")
        else:
            print("Order History:")
            for i, order in enumerate(self.orders):
                print(f"Order {i+1}:")
                for item in order:
                    print(f"{item.name} ({item.quantity}) [INR {item.price}]")
                print()

    def update_profile(self):
        # Implement logic to update user profile
        print("Profile updated successfully.")

# Create an instance of Admin
admin = Admin()

# Create an instance of User
user = User()

# Main program loop
while True:
    print("------ Food Ordering App ------")
    print("1. Admin Login")
    print("2. User Register")
    print("3. User Login")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Admin Login
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")
        # Implement logic to validate admin login credentials
        if admin_username == "admin" and admin_password == "admin123":
            print("Admin logged in successfully.")
            while True:
                print("------ Admin Menu ------")
                print("1. Add Food Item")
                print("2. Edit Food Item")
                print("3. View Food Items")
                print("4. Remove Food Item")
                print("5. Logout")

                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    name = input("Enter food item name: ")
                    quantity = input("Enter food item quantity: ")
                    price = float(input("Enter food item price: "))
                    discount = float(input("Enter food item discount: "))
                    stock = int(input("Enter food item stock: "))
                    admin.add_food_item(name, quantity, price, discount, stock)
                elif admin_choice == "2":
                    food_id = int(input("Enter food item ID to edit: "))
                    new_details = {}
                    new_name = input("Enter new name (leave blank to skip): ")
                    if new_name:
                        new_details["name"] = new_name
                    new_quantity = input("Enter new quantity (leave blank to skip): ")
                    if new_quantity:
                        new_details["quantity"] = new_quantity
                    new_price = input("Enter new price (leave blank to skip): ")
                    if new_price:
                        new_details["price"] = float(new_price)
                    new_discount = input("Enter new discount (leave blank to skip): ")
                    if new_discount:
                        new_details["discount"] = float(new_discount)
                    new_stock = input("Enter new stock (leave blank to skip): ")
                    if new_stock:
                        new_details["stock"] = int(new_stock)
                    admin.edit_food_item(food_id, new_details)
                elif admin_choice == "3":
                    admin.view_food_items()
                elif admin_choice == "4":
                    food_id = int(input("Enter food item ID to remove: "))
                    admin.remove_food_item(food_id)
                elif admin_choice == "5":
                    print("Admin logged out successfully.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid admin credentials. Please try again.")

    admin_choice = input("Enter your choice: ")

    if admin_choice == "1":

        name = input("Enter food item name: ")

        quantity = input("Enter food item quantity: ")

        price = float(input("Enter food item price: "))

        discount = float(input("Enter food item discount: "))

        stock = int(input("Enter food item stock: "))

        admin.add_food_item(name, quantity, price, discount, stock)

    elif admin_choice == "2":

        food_id = int(input("Enter food item ID to edit: "))

        new_details = {}

        new_name = input("Enter new name (leave blank to skip): ")

        if new_name:
            new_details["name"] = new_name

        new_quantity = input("Enter new quantity (leave blank to skip): ")

        if new_quantity:
            new_details["quantity"] = new_quantity

        new_price = input("Enter new price (leave blank to skip): ")

        if new_price:
            new_details["price"] = float(new_price)

        new_discount = input("Enter new discount (leave blank to skip): ")

        if new_discount:
            new_details["discount"] = float(new_discount)

        new_stock = input("Enter new stock (leave blank to skip): ")

        if new_stock:
            new_details["stock"] = int(new_stock)

        admin.edit_food_item(food_id, new_details)

    elif admin_choice == "3":

        admin.view_food_items()

    elif admin_choice == "4":

        food_id = int(input("Enter food item ID to remove: "))

        admin.remove_food_item(food_id)

    elif admin_choice == "5":

        print("Admin logged out successfully.")

        break

    else:

        print("Invalid choice. Please try again.")

else:

    print("Invalid admin credentials. Please try again.")