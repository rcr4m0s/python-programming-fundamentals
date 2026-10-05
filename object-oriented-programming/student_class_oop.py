class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_info(self):
        print(f"Student: {self.name} | Score: {self.score}")

    def get_status(self):
        if self.score >= 75:
            return "PASSED"
        else:
            return "FAILED"

student1 = Student("Alice", 88)
student2 = Student("Bob", 65)

student1.display_info()
student2.display_info()

print(f"{student1.name} Status: {student1.get_status()}")
print(f"{student2.name} Status: {student2.get_status()}")