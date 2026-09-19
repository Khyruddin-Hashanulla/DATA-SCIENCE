"""
Q4. Create a class Shape with a method area().
- Create subclasses Circle, Rectangle and Triangle that override the area() method.
"""

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4)
print(f"Circle Area: {circle.area()}")
print(f"Rectangle Area: {rectangle.area()}")
print(f"Triangle Area: {triangle.area()}")
