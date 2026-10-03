employees = [
    {"name": "Alice", "salary": 20000, "rating": 9},
    {"name": "Bob", "salary": 15000, "rating": 6},
    {"name": "Charlie", "salary": 25000, "rating": 8}
]



for money in employees:
    if money["rating"] >= 8:
        bonus = money["salary"] * 0.10
        money["salary"] += bonus
        print(f"{money["name"]} received a 10% bonus! New Salary: {money['salary']} ")
    elif money["rating"] < 8:
        print(f"{money["name"]} retains current salary: {money["salary"]}")
