from mars_rover_kata.cardinal_point import CardinalPoint


class Rover:
    def __init__(self, current_coordinates, planet):
        self.planet = planet
        self.current_coordinates = current_coordinates

    def instruct(self, commands):
        coordinates = self.current_coordinates
        for command in commands:
            coordinates = self.move(coordinates, command)
        self.current_coordinates = coordinates

    def move(self, coordinate, command):
        if command == 'f':
            return self.planet.move_towards(coordinate, coordinate.direction)
        elif command == 'b':
            return self.planet.move_towards(coordinate, coordinate.direction.invert())
        elif command == 'l':
            return self.turn_left(coordinate)
        elif command == 'r':
            return self.turn_right(coordinate)

    def locate(self):
        return self.current_coordinates

    def turn_left(self, coordinate):
        direction = coordinate.direction.next_point_anti_clockwise()
        return coordinate.adjust_by(direction=direction)

    def turn_right(self, coordinate):
        direction = coordinate.direction.next_point_clockwise()
        return coordinate.adjust_by(direction=direction)
