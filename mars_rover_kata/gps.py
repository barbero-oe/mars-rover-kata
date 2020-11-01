from enum import Enum


class GPS:
    def __init__(self, coordinate):
        self.coordinate = coordinate

    def current_coordinates(self):
        return self.coordinate

    def update(self, coordinate):
        self.coordinate = coordinate


class Coordinate:
    def __init__(self, latitude, longitude, direction):
        self.latitude = latitude
        self.longitude = longitude
        self.direction = direction

    def adjust_by(self, latitude=0, longitude=0, direction=None):
        return Coordinate(self.latitude + latitude,
                          self.longitude + longitude,
                          self.__update_direction(direction))

    def __update_direction(self, direction):
        return self.direction if direction is None else direction

    def __eq__(self, other):
        return (self.latitude == other.latitude
                and self.longitude == other.longitude
                and self.direction == other.direction)

    def __repr__(self):
        return f'LAT: {self.latitude} LON: {self.longitude} DIR: {self.direction}'


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
