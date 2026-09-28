

def analyze_inventory(inventory):
    total_value = 0
    most_expensive = inventory[0]  # Baseline para sa highest price

    print("\n--- INVENTORY REPORT ---")
    
    for item in inventory:
        # 1. Total Value
        item_value = item["price"] * item["stock"]
        total_value += item_value

        # 2. Out of Stock Check
        if item["stock"] == 0:
            print(f"Out of stock: {item['item']}")

        # 3. Most Expensive Check
        if item["price"] > most_expensive["price"]:
            most_expensive = item

    print(f"Total Value: ₱{total_value}")
    print(f"Most Expensive Item: {most_expensive['item']} (₱{most_expensive['price']})")


inventory = [
    {"item": "Apple", "price": 20, "stock": 5},
    {"item": "Banana", "price": 10, "stock": 0},
    {"item": "Orange", "price": 15, "stock": 12},
    {"item": "Mango", "price": 30, "stock": 0}
]

# Ipasa ang tamang variable na 'inventory'
analyze_inventory(inventory)