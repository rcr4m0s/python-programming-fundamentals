class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance 

    # Getter method
    def get_balance(self):
        return self.__balance

    def _set_balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₱{amount}. New Balance: ₱{self.__balance}")

class PremiumAccount(BankAccount):
    def withdraw(self, amount):
        current_balance = self.get_balance()
        if current_balance - amount >= -500:
            new_balance = current_balance - amount
            self._set_balance(new_balance)
            print(f"Withdrew ₱{amount}. New Balance: ₱{new_balance}")
        else:
            print("Overdraft limit exceeded!")


acc = PremiumAccount("Ramos", 1000)

acc.withdraw(1200)
acc.withdraw(400)  

print(f"Final Balance: ₱{acc.get_balance()}")