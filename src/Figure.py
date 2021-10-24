class Figure:

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('figure must be a Figure class instance')
        return self.area + figure.area
