class Order:
    def __init__(self, customer_name, food_price):
        self.customer_name = customer_name
        self.__food_price = food_price
    def get_food_price(self):
        return self.__food_price
    def calculate_total(self):
        return self.get_food_price()

class ExpressOrder(Order):
    def __init__(self, customer_name, food_price, delivery_distance_km):
        super().__init__(customer_name, food_price)
        self.delivery_distance_km = delivery_distance_km
    def calculate_total(self):
        base_price = super().calculate_total()
        deliv_fee = 50 + (self.delivery_distance_km * 10)
        return base_price + deliv_fee

# Regular Order
order1 = Order("Ramos", 300)
print(f"{order1.customer_name}'s Total: ₱{order1.calculate_total()}")
# Expected: 300

# Express Order (5 km distance)
order2 = ExpressOrder("Ramos Express", 300, 5)
print(f"{order2.customer_name}'s Total: ₱{order2.calculate_total()}")
# Expected: 400 (300 base + 50 delivery fee + [5 * 10])
        