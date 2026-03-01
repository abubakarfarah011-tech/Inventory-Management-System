# cli/router.py
# Router now only supports Admin functionality

from cli import menus
from products import LaptopService
from users.user_service import login  # function-based login

class Router:
    def __init__(self):
        self.laptop_service = LaptopService()

    def start(self):
        while True:
            email, password = menus.login_menu()

            success, user = login(email, password)
            if not success:
                print("Invalid credentials.")
                continue

            # Directly assume admin role
            print("\nLogged in as Admin.")
            self.admin_flow()

    # ======================
    # ADMIN FLOW
    # ======================
    def admin_flow(self):
        while True:
            choice = menus.admin_menu()

            if choice == "1":
                self.view_laptops()
            elif choice == "2":
                self.add_laptop()
            elif choice == "3":
                self.remove_laptop()
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Try again.")

    # ======================
    # COMMON FUNCTIONS
    # ======================
    def view_laptops(self):
        laptops = self.laptop_service.view_laptops()
        if not laptops:
            print("No laptops available.")
        else:
            for laptop in laptops:
                print(laptop)

    def add_laptop(self):
        name = input("Laptop name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        self.laptop_service.add_laptop(name, price, quantity)
        print("Laptop added successfully.")

    def remove_laptop(self):
        laptop_id = int(input("Enter laptop ID: "))
        self.laptop_service.remove_laptop(laptop_id)
        print("Laptop removed.")