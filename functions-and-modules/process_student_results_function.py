students_data = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 65},
    {"name": "Charlie", "score": 92},
    {"name": "David", "score": 70}
]

def processs_student_results(student_list):

    processed_students = []

    for item in student_list:

        score = item["score"]
        name = item["name"]

        if score >= 75:
            status =  "PASSED"
        else:
            status = "FAILED"
        new_student_dict = {
            "name": name, 
            "score": score, 
            "status": status
        }
        processed_students.append(new_student_dict)



    return processed_students

results = processs_student_results(students_data)
print(results)