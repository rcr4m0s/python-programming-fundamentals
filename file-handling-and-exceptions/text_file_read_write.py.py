# 1. MAGSULAT SA FILE
with open("notes.txt", "w") as file:
    file.write("Line 1: Python Core Mastered\n")
    file.write("Line 2: Functions and List Comprehensions Done\n")
    file.write("Line 3: Ready for OOP and Data Analysis\n")

# 2. MAGBASA MULA SA FILE
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)