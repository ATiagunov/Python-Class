class Box:

    box = []

    def put(self, obj):
        self.box.append(obj)

    def info(self):
        for obj in self.box:
            print(obj.name, obj.color, obj.size, sep=' ')


class Rectangle:

    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class Triangle:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class Sphere:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


box = Box()

rectangle1 = Rectangle('rectangle1', 'yellow', 10)
triangle1 = Triangle('triangle1', 'blue', 7)
sphere1 = Sphere('sphere1', 'green', 5)

figures = [rectangle1, triangle1, sphere1]
for f in figures:
    box.put(f)
box.info()