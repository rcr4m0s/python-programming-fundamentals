class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price  # Private variable!

    def get_price(self):
        return self.__price

    def _set_price(self, new_price):
        self.__price = new_price

    def get_discounted_price(self):
        return self.get_price()


class DiscountedProduct(Product):
    def get_discounted_price(self, discount_percentage):
        original_price = self.get_price()
        discounted = original_price * (1 - discount_percentage)
        return discounted


# Testing
item1 = Product("Mechanical Keyboard", 3000)
print(f"Item: {item1.name} | Price: ₱{item1.get_price()}")

item2 = DiscountedProduct("Gaming Monitor", 8000)
discounted = item2.get_discounted_price(0.15)
print(f"Item: {item2.name} | Original: ₱{item2.get_price()} | Discounted: ₱{discounted}")