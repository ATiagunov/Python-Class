class Box:
    name: str
    color: str
    size: int


class Rectangle(Box):
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class Triangle(Box):
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class Sphere(Box):
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


rectangle1 = Rectangle('rectangle1', 'yellow', 10)
triangle1 = Triangle('triangle1', 'blue', 7)
sphere1 = Sphere('sphere1', 'green', 5)

figures = [rectangle1, triangle1, sphere1]
for f in figures:
    print(isinstance(f, Box))
