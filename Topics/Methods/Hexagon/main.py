import math


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return round(((math.sqrt(3) * 3 / 2)) * self.side_length ** 2, 3)
