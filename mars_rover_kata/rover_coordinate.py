from mars_rover_kata.planet import PlanetCoordinates


class RoverCoordinate:
    def __init__(self, latitude, longitude, direction):
        self.latitude = latitude
        self.longitude = longitude
        self.direction = direction

    def coordinates(self):
        return PlanetCoordinates(self.latitude, self.longitude)

    def adjust_by(self, latitude=0, longitude=0, direction=None):
        return RoverCoordinate(self.latitude + latitude,
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
