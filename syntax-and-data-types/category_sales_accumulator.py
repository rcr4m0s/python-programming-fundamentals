sales = [
    {"item": "Laptop", "price": 35000, "category": "electronics"},
    {"item": "Shirt", "price": 500, "category": "apparel"},
    {"item": "Mouse", "price": 800, "category": "electronics"},
    {"item": "Jeans", "price": 1200, "category": "apparel"},
    {"item": "Headphones", "price": 2500, "category": "electronics"}
]

category_totals = {}

for item in sales:
    cat = item["category"]
    price = item["price"]

    if cat in category_totals:
        category_totals[cat] += price
    else:
        category_totals[cat] = price

print(f"Category Sales Summary: {cat}: {category_totals[cat]} {category_totals} ")