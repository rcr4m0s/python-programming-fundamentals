class Vehicle:
    def __init__(self, brand, rental_rate):
        self.brand = brand
        self.__rental_rate = rental_rate

    def get_rate(self):
        return self.__rental_rate

    def calculate_rate(self, days):
        return days * self.get_rate()


class LuxuryCar(Vehicle):
    def calculate_rate(self, days):
        base_rent = super().calculate_rate(days)
        return base_rent + 1000

car = Vehicle("Toyota", 1500)
print(f"Toyota Rent (3 days): {car.calculate_rate(3)}")

luxury = LuxuryCar("BMW", 5000)
print(f"BMW Rent (3 days): {luxury.calculate_rate(3)}")
                   