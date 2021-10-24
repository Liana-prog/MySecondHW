from src.Figure import Figure


class Rectangle(Figure):
    name = 'Rectangle'

    def __init__(self, a, b: int):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return (self.a + self.b) * 2
