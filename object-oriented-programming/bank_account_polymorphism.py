class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter / Helper para mabago ang private balance sa loob ng class methods
    def _set_balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₱{amount}. New Balance: ₱{self.__balance}")

# Child Class na may Polymorphism (Overriding)
class PremiumAccount(BankAccount):
    def withdraw(self, amount):
        # Kunin ang current balance gamit ang get_balance()
        current_balance = self.get_balance()
        
        # Pinapayagan maging negative hanggang -500
        if current_balance - amount >= -500:
            new_balance = current_balance - amount
            self._set_balance(new_balance)
            print(f"Withdrew ₱{amount}. New Balance: ₱{new_balance}")
        else:
            print("Overdraft limit exceeded!")

# --- Testing ---
acc = PremiumAccount("Ramos", 1000)

acc.withdraw(1200) # Pasok sa overdraft! Balance becomes -200
acc.withdraw(400)  # Sobra na sa -500 limit (-600)! Dapat ma-reject

print(f"Final Balance: ₱{acc.get_balance()}")