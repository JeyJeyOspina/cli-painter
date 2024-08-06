import matplotlib.pyplot as plt
import math
class Point:
    '''Inicializador o constructor de la clase'''
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y
class Circle:
    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius

    def area(self, center: Point, radius: float) -> float:
        area = (self.radius ** 2) * math.pi
        return area
    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self, x: float, y: float, r: float):
        return "Circle with center at ", self.center.x, self.center.y, "and radius ", self.radius

class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.point_1: Point = a
        self.point_2: Point = b
        self.point_3: Point = c

'''    def area(self, ):'''