import json
import os
from  users.user_model import User

FILE_PATH = os.path.join(os.path.dirname(__file__), "users.json")


def load_users():
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
            return [User(user["email"], user["password"]) for user in data]
    except (json.JSONDecodeError, FileNotFoundError):
        return []
    
def save_users(users):
    with open(FILE_PATH, "w") as file:
        json.dump([u.to_dict() for u in users],file,indent=4)
        
def register(email, password):
    users = load_users()
    
    for u in users:
       if u.get_email() == email:
        return False, "Email already exists."
    
    new_user = User(email,password)
    users.append(new_user)
    save_users(users)
    
    return True, "User registered successfully."

def login(email, password):
    users = load_users()
    
    for u in users:
        if u.get_email() == email and u.get_password() == password:
            return True, u
        
        return False, None
    
def update_password(email, new_password):
    users = load_users()
    
    for u in users:
        if u.get_email() == email:
            u.set_password(new_password)
            save_users(users)
            return True, "Password updated successfully."
        
        return False, "User not found."

if __name__ == "__main__":
    print("Running user_service test...\n")
    
success, message = register("abdi@gmail.com", "abdi234")
print("Register:", success,message)

success, user = login("abdi@gmail.com", "abdi234")
print("Login:",success)
    
success, message = update_password("abdi@gmail.com", "newpassword")
print("Update Password:", success,message)

success,user = login("abdi@gmail.com", "newpassword")
print("Login with new password:", success)
    
    
    
    