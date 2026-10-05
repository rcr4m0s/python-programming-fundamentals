class Subscription:
    def __init__(self, user, price):
        self.user = user
        self.__price = price

    def get_price(self):
        return self.__price
    def get_total_cost(self):
        return self.get_price()

class FamilyPlan(Subscription):
    def __init__(self, user, price, members):
        super().__init__(user, price)
        self.members = members


    def get_total_cost(self):
        base_price = super().get_total_cost()
        return base_price + (self.members * 100)

basic = Subscription("Ramos", 250)
print(f"{basic.user}'s Total: ₱{basic.get_total_cost()}")
# Expected: 250

family = FamilyPlan("Ramos Family", 250, 4)
print(f"{family.user}'s Total: ₱{family.get_total_cost()}")
