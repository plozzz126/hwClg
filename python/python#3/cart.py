class Cart():
    def __init__(self):
        self.cart = []

    def add_prod(self, Product):
        self.cart.append(Product)

    def get_cart(self):
        return self.cart

    def inf_pr(self):
        for product in self.cart:
            print(product.get_p())

    def total(self):
        total = 0

        for product in self.cart:
            total += product.price 
        return total

    def clear(self):
        self.cart.clear()
    