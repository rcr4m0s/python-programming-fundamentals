class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("WITHDREWED")
        else:
            print("Insufficient Funds!")

    def get_balance(self):
        return self.balance

account = BankAccount("Ramos", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)

print(f"Final Balance for {account.owner}: {account.balance}")