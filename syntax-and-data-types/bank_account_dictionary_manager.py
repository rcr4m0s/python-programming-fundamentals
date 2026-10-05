account = {
    "owner": "Student",
    "balance": 1000.0,
    "history": []
}


def deposit(acc, amount):
    acc["balance"] += amount
    acc["history"].append(f"Deposited ₱{amount}")


def withdraw(acc, amount):
    if acc["balance"] >= amount:
        acc["balance"] -= amount
        acc["history"].append(f"Withdrew ₱{amount}")
    else:
        print(f"\n⚠️ Cannot withdraw ₱{amount}: Insufficient funds!")


def display_summary(acc):
    print("\n--- BANK ACCOUNT SUMMARY ---")
    print(f"Owner: {acc['owner']}")
    print(f"Current Balance: ₱{acc['balance']}")

    print("\n--- TRANSACTION HISTORY ---")
    for item in acc["history"]:
        print(f"- {item}")


deposit(account, 500)
withdraw(account, 200)
withdraw(account, 2000)  
display_summary(account)