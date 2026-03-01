class Laptop:
    def __init__(self, laptop_id, name, price, quantity):
        self.__id = laptop_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    # ===== GETTERS =====
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    # ===== SETTER (for updating quantity) =====
    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            raise ValueError("Quantity cannot be negative")

    # ===== Convert to dictionary for JSON =====
    def to_dict(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "price": self.__price,
            "quantity": self.__quantity
        }

    # ===== String Representation =====
    def __str__(self):
        return f"ID: {self.__id} | {self.__name} | ${self.__price} | Stock: {self.__quantity}"