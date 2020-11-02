class Coordinate:
    def __init__(self, latitude, longitude, direction):
        self.latitude = latitude
        self.longitude = longitude
        self.direction = direction

    def adjust_by(self, latitude=0, longitude=0, direction=None):
        return Coordinate(self.latitude + latitude,
                          self.longitude + longitude,
                          self.__update_direction(direction))

    def update(self, latitude=None, longitude=None, direction=None):
        return Coordinate(self.__update_latitude(latitude),
                          self.__update_longitude(longitude),
                          self.__update_direction(direction))

    def __update_latitude(self, latitude):
        return self.latitude if latitude is None else latitude

    def __update_longitude(self, longitude):
        return self.longitude if longitude is None else longitude

    def __update_direction(self, direction):
        return self.direction if direction is None else direction

    def __eq__(self, other):
        return (self.latitude == other.latitude
                and self.longitude == other.longitude
                and self.direction == other.direction)

    def __repr__(self):
        return f'LAT: {self.latitude} LON: {self.longitude} DIR: {self.direction}'
