import math
from src.Figure import Figure


class Circle(Figure):
    name = 'Circle'

    def __init__(self, r: int):
        self.r = r

    @property
    def area(self):
        return math.pi*(self.r**2)

    @property
    def perimeter(self):
        return 2*math.pi*self.r
