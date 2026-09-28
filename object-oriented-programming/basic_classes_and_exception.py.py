try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")



point = Point(10, 20)
point.x = 11
print(point.x)


class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()


class Mammal:
    def walk():
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("be annoying")

dog1 = Dog()
dog1.walk()


cat1 = Cat()














