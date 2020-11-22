from enum import Enum


class CardinalPoint(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

    def next_point_anti_clockwise(self):
        if self == CardinalPoint.NORTH:
            return CardinalPoint.WEST
        elif self == CardinalPoint.WEST:
            return CardinalPoint.SOUTH
        elif self == CardinalPoint.SOUTH:
            return CardinalPoint.EAST
        elif self == CardinalPoint.EAST:
            return CardinalPoint.NORTH

    def next_point_clockwise(self):
        if self == CardinalPoint.NORTH:
            return CardinalPoint.EAST
        elif self == CardinalPoint.EAST:
            return CardinalPoint.SOUTH
        elif self == CardinalPoint.SOUTH:
            return CardinalPoint.WEST
        elif self == CardinalPoint.WEST:
            return CardinalPoint.NORTH

    @staticmethod
    def from_letter(letter):
        if letter == 'N':
            return CardinalPoint.NORTH
        elif letter == 'S':
            return CardinalPoint.SOUTH
        elif letter == 'E':
            return CardinalPoint.EAST
        elif letter == 'W':
            return CardinalPoint.WEST
