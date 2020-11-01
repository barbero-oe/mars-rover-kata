from mars_rover_kata.gps import Coordinate, Direction


class PositionBuilder:
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.orientation = None

    def facing_north(self):
        self.orientation = Direction.NORTH
        return self

    def move_south(self, units):
        self.y -= units
        return self

    def move_north(self, units):
        self.y += units
        return self

    def build(self):
        return Coordinate(self.x, self.y, self.orientation)


def initial_position():
    return PositionBuilder(5, 5)
