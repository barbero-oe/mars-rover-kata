from mars_rover_kata.gps import Coordinate, Direction


class PositionBuilder:
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.orientation = None

    def facing(self, cardinal_point):
        self.orientation = Direction.from_letter(cardinal_point)
        return self

    def move(self, movement):
        self.x += movement[0]
        self.y += movement[1]
        return self

    def build(self):
        return Coordinate(self.x, self.y, self.orientation)


def initial_position():
    return PositionBuilder(5, 5)
