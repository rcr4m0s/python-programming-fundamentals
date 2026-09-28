def analyze_grades(grades):
    failed_count = 0
    total = 0
    highest_grade = grades[0]
    lowest_grade = grades[0]
    for grade in grades:
        total += grade
        if grade > highest_grade:
            highest_grade = grade
            
        elif grade < lowest_grade:
            lowest_grade = grade
        
        elif grade < 75:
            failed_count += 1


    average = total / len(grades)
    if average < 75:
        remarks = "FAILED"
    else:
        remarks = "PASSED"

    print("---Grade Report---")
    print(f"Highest Grade: {highest_grade}")
    print(f"Lowest Grade: {lowest_grade}")
    print(f"Average: {average}")
    print(f"Remaks: {remarks}")
    print(f"Failed Subjects: {failed_count}")


user_type = []

for i in range (4):
    grado = float(input(f"Enter grade for Subject {i + 1}: "))
    user_type.append(grado)

analyze_grades(user_type)