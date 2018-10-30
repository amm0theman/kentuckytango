"""#Point class representing a point on the asteroids map"""


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __mul__(self, modifier: float):
        x = self.x * modifier
        y = self.y * modifier
        return Point(x, y)
