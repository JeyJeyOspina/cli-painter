import matplotlib.pyplot as plt
import math
import pickle


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius

    def area(self) -> float:
        area = (self.radius ** 2) * math.pi
        return area

    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self) -> str:
        return f"Circle with center at  {self.center.x} {self.center.y}, and radius, {self.radius}"


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.point_1: Point = a
        self.point_2: Point = b
        self.point_3: Point = c

    def area(self) -> float:
        area = 0.5 * (self.point_1.x * self.point_2.y + self.point_2.x * self.point_3.y +
                      self.point_3.x * self.point_1.y - self.point_2.x * self.point_1.y -
                      self.point_3.x * self.point_2.y - self.point_1.x * self.point_3.y)
        return area

    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
        plt.fill(x, y, color='b')
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        return (f"Triangle with vertices at ({self.point_1.x}, {self.point_1.y}), ({self.point_2.x},"
                f" {self.point_2.y}) and ({self.point_3.x}, {self.point_3.y})")


class Rectangle:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1: Point = point_1
        self.point_2: Point = point_2

    def area(self) -> float:
        area = 0.5 * (self.point_2.x * self.point_2.y - self.point_1.x * self.point_2.y -
                      self.point_2.x * self.point_1.y + self.point_1.x * self.point_1.y)
        return area

    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_2.x, self.point_1.x, self.point_1.x]
        y = [self.point_1.y, self.point_1.y, self.point_2.y, self.point_2.y, self.point_1.y]
        plt.fill(x, y, color='g')
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        return (f"Rectangle with vertices at ({self.point_1.x}, {self.point_1.y}) and "
                f"({self.point_2.x}, {self.point_2.y})")


class Painter:

    FILE = ".painter"

    def __init__(self) -> None:
        self.shapes: list = []
        self._load()

    def _load(self) -> None:
        try:
            with open(Painter.FILE, "rb") as f:
                self.shapes = pickle.load(f)
        except (EOFError, FileNotFoundError):
            self.shapes = []

    def _save(self) -> None:
        with open(Painter.FILE, "wb") as f:
            pickle.dump(self.shapes, f)

    def add_shape(self, shape) -> None:
        self.shapes.append(shape)
        self._save()

    def total_area(self) -> float:
        return sum(shape.area() for shape in self.shapes)

    def clear(self) -> None:
        self.shapes = []
        self._save()
