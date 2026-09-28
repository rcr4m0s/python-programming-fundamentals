inventory = [
    {"item": "Laptop", "price": 30000, "stock": 5},
    {"item": "Mouse", "price": 500, "stock": 0},
    {"item": "Keyboard", "price": 1500, "stock": 3}
]


for invent in inventory:
    if invent["stock"] > 0:
        print(f"{invent["item"]} - IN STOCK (Total Value: {invent["price"] * invent["stock"]})" )
    elif invent["stock"] == 0:
        print(f"{invent["item"]} - OUT OF STOCK!")




print("ENDABLE")