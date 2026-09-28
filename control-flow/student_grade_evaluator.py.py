students = [
    {"name": "Alice", "scores": [85, 90, 92]},
    {"name": "Bob", "scores": [70, 65, 72]},
    {"name": "Charlie", "scores": [95, 98, 100]}
]

for item in students:
    average = round(sum(item["scores"]))/len(item["scores"])
    if average >= 85:
        print(f"{item["name"]} - {average} | Status: PASSED WITH HONORS")
    elif average >= 75 and average < 85:
        print(f"{item["name"]} - {average} | Status: PASSED")
    else:
        print(f"{item["name"]} - {average} | Status: FAILED")

