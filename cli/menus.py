# cli/menus.py
# Displays CLI menus and collects user input for login and admin dashboard

def login_menu():
    print("\n LOGIN ")
    email = input("Email: ")
    password = input("Password: ")
    return email, password


def admin_menu():
    print("\n ADMIN MENU ")
    print("1. View Laptops")
    print("2. Add Laptop")
    print("3. Remove Laptop")
    print("4. Logout")
    return input("Enter choice: ")