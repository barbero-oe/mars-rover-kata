from mars_rover_kata.cardinal_point import CardinalPoint


class Planet:
    PLANET_SIZE = 10

    def move_towards(self, coordinates, cardinal_point):
        if cardinal_point == CardinalPoint.SOUTH:
            return self.cross_south_longitude(coordinates)
        elif cardinal_point == CardinalPoint.NORTH:
            return self.cross_north_longitude(coordinates)
        elif cardinal_point == CardinalPoint.EAST:
            return coordinates.adjust_by(latitude=1)
        elif cardinal_point == CardinalPoint.WEST:
            return coordinates.adjust_by(latitude=-1)

    def cross_south_longitude(self, coordinates):
        result = coordinates.longitude - 1
        if result >= 1:
            return coordinates.update(longitude=result)
        else:
            return coordinates.update(latitude=Planet.PLANET_SIZE - (coordinates.latitude - 1),
                                      direction=coordinates.direction.invert())

    def cross_north_longitude(self, coordinates):
        result = coordinates.longitude + 1
        if result <= Planet.PLANET_SIZE:
            return coordinates.update(longitude=result)
        else:
            return coordinates.update(latitude=Planet.PLANET_SIZE - (coordinates.latitude - 1),
                                      direction=coordinates.direction.invert())

    # def move_on_latitude_towards_east(self, coordinates):
    #     result = coordinates.longitude + 1
    #     if result <= Planet.PLANET_SIZE:
    #         return coordinates.update(longitude=result)
    #     else:
    #         return coordinates.update(longitude=1,
    #                                   direction=coordinates.direction.invert())
