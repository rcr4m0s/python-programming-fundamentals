cart = [
    {"item": "Shirt", "price": 500, "category": "clothing"},
    {"item": "Jeans", "price": 1200, "category": "clothing"},
    {"item": "Shoes", "price": 2500, "category": "footwear"},
    {"item": "Socks", "price": 150, "category": "footwear"}
]

grand_total = 0

for item in cart:

    if item["category"] == "clothing":
        discounted = item["price"] * 0.8
        print(f"{item["item"]} ({item["category"]}) - Discounted Price: {discounted} ")
        grand_total += discounted
    else:
        print(f"{item["item"]} ({item["category"]}) - Regular Price: {item["price"]}")
        grand_total += item["price"]
print(f"Grand Total: {grand_total}")