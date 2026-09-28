class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.__base_salary = base_salary

    def get_salary(self):
        return self.__base_salary
    def calculate_pay(self):
        return self.get_salary()


class Manager(Employee):
    def calculate_pay(self):
        supah = super().calculate_pay()
        return supah + 5000

emp = Employee("Juan", 2000)
print(f"{emp.name}'s Pay: {emp.calculate_pay()}")

mgr = Manager("Ramos", 35000)
print(f"{mgr.name}'s Pay: {mgr.calculate_pay()}")