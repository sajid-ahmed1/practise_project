import polars as pl

class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(title)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task index.")

    def show_tasks(self):
        print("Your Tasks:")
        for i, tasks in enumerate(self.tasks, start=1):
            print(f"{i}. {tasks}")


class Person:
    def __init__(self, name, age):   # runs when you create a Person
        self.name = name             # attribute
        self.age = age               # attribute

    def greet(self):                 # method
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

#Polymorphism example
class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


if __name__ == "__main__":
    todo = Todo()
    todo.add_task("Learn Python classes")
    todo.add_task("Run code inside Docker")
    todo.show_tasks()

