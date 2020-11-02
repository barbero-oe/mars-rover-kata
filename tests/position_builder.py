from mars_rover_kata.cardinal_point import CardinalPoint
from mars_rover_kata.coordinate import Coordinate


class PositionBuilder:
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.orientation = None

    def facing(self, cardinal_point):
        self.orientation = CardinalPoint.from_letter(cardinal_point)
        return self

    def move(self, movement):
        self.x += movement[0]
        self.y += movement[1]
        return self

    def build(self):
        return Coordinate(self.x, self.y, self.orientation)


def initial_position():
    return PositionBuilder(5, 5)


def origin_position():
    return PositionBuilder(1, 1)


def position_at(coordinate):
    return PositionBuilder(coordinate[0], coordinate[1]).facing(coordinate[2])
