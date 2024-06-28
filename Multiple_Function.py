import sympy as sp
from Point import Point


class MultipleFunction:

    def __init__(self, function) -> None:
        self.function = sp.sympify(function)
        self.x, self.y, self.z = sp.symbols("x,y,z")
        self.symbols = []

    def set_symbols(self, symbols: list):
        for symbol in symbols:
            self.symbols.append(sp.symbols(str(symbol)))

    def get_gradian(self) -> str:
        x = sp.diff(self.function, self.x)
        y = sp.diff(self.function, self.y)
        z = sp.diff(self.function, self.z)
        return f"({x})i + ({y})j + ({z})k"

    def get_gradian_value(self, point: Point) -> Point:
        x = sp.diff(self.function, self.x)
        y = sp.diff(self.function, self.y)
        z = sp.diff(self.function, self.z)

        i = x.subs(self.x, point.x)
        j = y.subs(self.y, point.y)
        k = z.subs(self.z, point.z)

        return Point(i, j, k)

    def get_gradian_n_value(self, point: Point) -> Point:
        differentials = []
        for symbol in self.symbols:
            differentials.append(sp.diff(self.function, symbol))

        gradian = []
        i = 0
        for differential in differentials:
            gradian.append(differential.subs(self.symbols[i], point.multi[i]))

        point = Point()
        point.set_multi(gradian)
        return point
