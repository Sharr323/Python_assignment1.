#Question 1

class Vehicle:
    def start_engine(self):
        print("Starting the vehicle engine...")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key ignition.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with kick start.")

# Example
v = Vehicle()
c = Car()
b = Bike()

v.start_engine()
c.start_engine()
b.start_engine()


#Question 2

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.1416 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

def total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)

# User input
shapes = []
n = int(input("How many shapes do you want to enter? "))

for _ in range(n):
    shape_type = input("Enter shape type (circle/rectangle): ").strip().lower()
    if shape_type == "circle":
        r = float(input("Enter radius: "))
        shapes.append(Circle(r))
    elif shape_type == "rectangle":
        w = float(input("Enter width: "))
        h = float(input("Enter height: "))
        shapes.append(Rectangle(w, h))

print("Total Area:", total_area(shapes))


#Question 3

class Shape:
    def __init__(self):
        print("Shape initialized")

    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()  # Call Shape's constructor
        self.width = width
        self.height = height

    def calculate_area(self):
        super().__init__()  # Demonstrating super() inside method
        return self.width * self.height

# Example
r = Rectangle(4, 6)
print("Rectangle Area:", r.calculate_area())


#Question 4
class Dog:
    def make_sound(self):
        print("Woof!")

class Cat:
    def make_sound(self):
        print("Meow!")

def process_sound(sound_object):
    sound_object.make_sound()

# Example
dog = Dog()
cat = Cat()

process_sound(dog)
process_sound(cat)

#Question 5

from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

class TextFileHandler(FileHandler):
    def read(self):
        print("Reading text file...")

    def write(self, data):
        print(f"Writing to text file: {data}")

class BinaryFileHandler(FileHandler):
    def read(self):
        print("Reading binary file...")

    def write(self, data):
        print(f"Writing to binary file: {data}")

# Example
text_handler = TextFileHandler()
binary_handler = BinaryFileHandler()

text_handler.read()
text_handler.write("Hello World")

binary_handler.read()
binary_handler.write(b'\x00\xFF')


