import json
import os
from products.laptop_models import Laptop


class LaptopService:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "laptops.json")
        self.laptops = self.load_laptops()

    # ==========================
    # LOAD & SAVE
    # ==========================

    def load_laptops(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return [
                    Laptop(l["id"], l["name"], l["price"], l["quantity"])
                    for l in data
                ]
        except FileNotFoundError:
            return []

    def save_laptops(self):
        with open(self.file_path, "w") as file:
            json.dump(
                [laptop.to_dict() for laptop in self.laptops],
                file,
                indent=4
            )

    # ==========================
    # ADMIN FUNCTIONS (CRUD)
    # ==========================

    # CREATE
    def add_laptop(self, name, price, quantity):
        new_id = self.generate_id()
        new_laptop = Laptop(new_id, name, price, quantity)
        self.laptops.append(new_laptop)
        self.save_laptops()
        return new_laptop

    # DELETE
    def remove_laptop(self, laptop_id):
        for laptop in self.laptops:
            if laptop.get_id() == laptop_id:
                self.laptops.remove(laptop)
                self.save_laptops()
                return True
        return False

    # ==========================
    # CUSTOMER FUNCTIONS
    # ==========================

    # READ
    def view_laptops(self):
        return self.laptops

    # UPDATE (Reduce quantity after purchase)
    def reduce_quantity(self, laptop_id, amount):
        for laptop in self.laptops:
            if laptop.get_id() == laptop_id:
                if laptop.get_quantity() >= amount:
                    laptop.set_quantity(
                        laptop.get_quantity() - amount
                    )
                    self.save_laptops()
                    return True
                else:
                    return False
        return False

    # ==========================
    # HELPER METHODS
    # ==========================

    def generate_id(self):
        if not self.laptops:
            return 1
        return max(laptop.get_id() for laptop in self.laptops) + 1

    def find_by_id(self, laptop_id):
        for laptop in self.laptops:
            if laptop.get_id() == laptop_id:
                return laptop
        return None