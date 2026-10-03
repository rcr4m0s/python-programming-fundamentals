class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_info(self):
        print(f"Student: {self.name} | Score: {self.score}")

    # Bagong Method: Titingnan kung PASSED o FAILED
    def get_status(self):
        if self.score >= 75:
            return "PASSED"
        else:
            return "FAILED"

# --- Testing Section ---
student1 = Student("Alice", 88)
student2 = Student("Bob", 65)

# 1. I-print ang info
student1.display_info()
student2.display_info()

# 2. I-print ang status gamit ang get_status()
print(f"{student1.name} Status: {student1.get_status()}")
print(f"{student2.name} Status: {student2.get_status()}")