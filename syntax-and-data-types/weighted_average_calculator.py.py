grades = [
    {"subject": "Math", "grade": 85, "units": 3},
    {"subject": "English", "grade": 90, "units": 3},
    {"subject": "Science", "grade": 88, "units": 4}
]

total_points = 0
total_units = 0

for item in grades:
    points = item["grade"] * item["units"]
    total_points += points
    total_units += item["units"]

    print(f"{item["subject"]} ({item["units"]} units) :  Grade: {item["grade"]} -> Points: {points} ")


average = total_points/total_units

print(f"Weighted Average: {average}")

