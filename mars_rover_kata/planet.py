class Planet:
    PLANET_SIZE = 10


class PlanetMap(object):
    def __init__(self, max_coordinate):
        self.max_coordinate = PlanetCoordinates(max_coordinate[0], max_coordinate[1])

    def get_absolute_coordinate(self, coord, relative_movement):
        latitude = coord.latitude + relative_movement[0]
        longitude = coord.longitude + relative_movement[1]
        return PlanetCoordinates(latitude, longitude)


class PlanetCoordinates:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
