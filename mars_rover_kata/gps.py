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


class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

    @staticmethod
    def from_letter(letter):
        if letter == 'N':
            return Direction.NORTH
        elif letter == 'S':
            return Direction.SOUTH
        elif letter == 'E':
            return Direction.EAST
        elif letter == 'W':
            return Direction.WEST
