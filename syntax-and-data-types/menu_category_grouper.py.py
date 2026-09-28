menu = [
    {"name": "Burger", "category": "Food"},
    {"name": "Iced Tea", "category": "Drinks"},
    {"name": "Fries", "category": "Food"},
    {"name": "Coffee", "category": "Drinks"},
    {"name": "Sundae", "category": "Dessert"}
]

grouped_menu = {}

for item in menu:
    cat = item["category"]
    name = item["name"]

    if cat in grouped_menu:
        grouped_menu[cat].append(name)
    else:
        grouped_menu[cat] = [name]

print(grouped_menu)