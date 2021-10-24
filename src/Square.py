from src.Figure import Figure


class Square(Figure):
    name = 'Square'

    def __init__(self, a: int):
        self.a = a

    @property
    def area(self):
        return self.a ** 2

    @property
    def perimeter(self):
        return self.a * 4
