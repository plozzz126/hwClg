class Product():
    def __init__(self, prod_name, price):
        self.prod_name = prod_name
        self.price = price

    def get_p(self):
        if hasattr(self, "size"):
            return self.prod_name, self.price, self.size
        elif hasattr(self, "volume"):
            return self.prod_name, self.price, self.volume
        return self.prod_name, self.price

    def set_p(self, prod_name, price):
        self.prod_name = prod_name
        self.price = price
    
class Pizza(Product):
    def __init__(self, prod_name, price, size):
        super().__init__(prod_name, price)
        self.size = size

class Drink(Product):
    def __init__(self, prod_name, price, volume):
        super().__init__(prod_name, price)
        self.volume = volume