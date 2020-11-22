from mars_rover_kata.navigation import Navigation
from mars_rover_kata.planet import PlanetCoordinates
from mars_rover_kata.rover_coordinate import RoverCoordinate


class Rover:
    def __init__(self, rover_location, planet_map):
        self.planet_map = planet_map
        self.rover_location = rover_location

    def instruct(self, commands):
        coordinates = self.rover_location
        for command in commands:
            coordinates = self.move(coordinates, command)
        self.rover_location = coordinates

    def move(self, coordinate, command):
        if command == 'l':
            return self.turn_left(coordinate)
        elif command == 'r':
            return self.turn_right(coordinate)

    def locate(self):
        return self.rover_location

    def turn_left(self, coordinate):
        direction = coordinate.direction.next_point_anti_clockwise()
        return coordinate.adjust_by(direction=direction)

    def turn_right(self, coordinate):
        direction = coordinate.direction.next_point_clockwise()
        return coordinate.adjust_by(direction=direction)

    def command(self, commands):
        for command in commands:
            if command == 'f':
                nav = Navigation()
                relative_movement = nav.move_forward(self.rover_location.direction)
                location: PlanetCoordinates = self.planet_map \
                    .get_absolute_coordinate(self.rover_location.coordinates(), relative_movement)
                self.rover_location = RoverCoordinate(location.latitude, location.longitude,
                                                      self.rover_location.direction)
            elif command == 'b':
                nav = Navigation()
                relative_movement = nav.move_backwards(self.rover_location.direction)
                location: PlanetCoordinates = self.planet_map \
                    .get_absolute_coordinate(self.rover_location.coordinates(), relative_movement)
                self.rover_location = RoverCoordinate(location.latitude, location.longitude,
                                                      self.rover_location.direction)
