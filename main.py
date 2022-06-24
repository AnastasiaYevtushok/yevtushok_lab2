import math
import abc


def numValidation(value):
    if value < 0:
        raise ValueError("Name cannot be lower then 0")
    return value


class Shape:
    def __init__(self, name):
        self.name = name

    @abc.abstractclassmethod
    def area(self):
        pass

    @abc.abstractclassmethod
    def perimeter(self):
        pass

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = numValidation(length)

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.length * 4


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = numValidation(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rhombus(Shape):
    def __init__(self, d1, d2):
        super().__init__("Rhombus")
        self.d1 = numValidation(d1)
        self.d2 = numValidation(d2)

    def area(self):
        return (self.d1 * self.d2) / 2

    def perimeter(self):
        return 2 * math.sqrt((self.d1 ** 2) + (self.d2 ** 2))
