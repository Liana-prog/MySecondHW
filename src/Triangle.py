from cmath import sqrt
from src.Figure import Figure


class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, a, b, c: int):
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        pp = ((self.a + self.b + self.c)/2)
        return sqrt(pp * (pp - self.a) * (pp - self.b) * (pp - self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    def __new__(cls, a, b, c):
        if (a < b + c) and (b < a + c) and (c < a + b):
            instance = super(Triangle, cls).__new__(cls)
            instance.a = a
            instance.b = b
            instance.c = c
            return instance
        else:
            return None
