students = [
    {"name": "Alice", "average": 88},
    {"name": "Bob", "average": 65},
    {"name": "Charlie", "average": 92},
    {"name": "David", "average": 72},
    {"name": "Eve", "average": 78}
]


status_counts = {"Passed": 0, "Failed": 0}

for item in students:
    average = item["average"]
    if average >= 75:
        status_counts["Passed"] += 1
    else:
        status_counts["Failed"] += 1

print(f"{status_counts}")