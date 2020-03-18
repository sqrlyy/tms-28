from math import sqrt


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


class Figure:
    pass


class Circle(Figure):

    def __init__(self, point, radius):
        self.coord = point
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def square(self):
        return 3.14 * self.radius ** 2


class Triangle(Figure, Point):

    def __init__(self, point1, point2, point3):
        self.first_coord = point1
        self.second_coord = point2
        self.third_coord = point3
        self.first_line = sqrt(
            (self.first_coord.x - self.second_coord.x) ** 2 + (self.first_coord.y - self.second_coord.y) ** 2)
        self.second_line = sqrt(
            (self.first_coord.x - self.third_coord.x) ** 2 + (self.first_coord.y - self.third_coord.y) ** 2)
        self.third_line = sqrt(
            (self.second_coord.x - self.third_coord.x) ** 2 + (self.second_coord.y - self.third_coord.y) ** 2)

    def perimeter(self):
        return self.first_line + self.second_line + self.third_line

    def square(self):
        p = Triangle.perimeter(self) / 2
        return sqrt(p * (p - self.first_line) * (p - self.second_line) * (p - self.third_line))


class Square(Figure, Point):
    def __init__(self, point1, point2):
        self.first_coord = point1
        self.second_coord = point2
        self.line = sqrt(
            (self.first_coord.x - self.second_coord.x) ** 2 +
            (self.first_coord.y - self.second_coord.y) ** 2) / sqrt(2)

    def perimeter(self):
        return self.line * 4

    def square(self):
        return self.line ** 2
