class Figure:
    unit = "см"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    p = 3.1415

    def __init__(self, radius):
        super(Circle, self).__init__()
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        __radius = value

    def calculate_area(self):
        return round(self.p * (self.__radius ** 2), 2)

    def info(self):
        return f"Circle radius - {self.__radius}, area - {self.calculate_area()}"


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super(RightTriangle, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        __side_a = value

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        __side_b = value

    def calculate_area(self):
        return round(1 / 2 * (self.side_a * self.__side_b), 2)

    def info(self):
        return f"side_a {self.__side_a} side_b {self.__side_b} area {self.calculate_area()}"



circle = Circle(3)
circle2 = Circle(9)

triangle = RightTriangle(5, 10)
triangle2 = RightTriangle(7, 14)
triangle3 = RightTriangle(2, 6)

figurs = [circle, circle2, triangle, triangle2, triangle3]

for figure in figurs:
    print(figure.info())