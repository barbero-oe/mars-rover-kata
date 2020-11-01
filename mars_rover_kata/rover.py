from mars_rover_kata.gps import CardinalPoint


class Rover:
    def __init__(self, gps):
        self.gps = gps

    def instruct(self, commands):
        coordinates = self.gps.current_coordinates()
        for command in commands:
            coordinates = self.move(command, coordinates)
        self.gps.update(coordinates)

    def move(self, command, coordinates):
        if command == 'f':
            return self.forward(coordinates)
        elif command == 'b':
            return self.backward(coordinates)
        elif command == 'l':
            return self.turn_left(coordinates)
        elif command == 'r':
            return self.turn_right(coordinates)

    def forward(self, coordinates):
        if coordinates.direction == CardinalPoint.NORTH:
            return coordinates.adjust_by(longitude=1)
        elif coordinates.direction == CardinalPoint.SOUTH:
            return coordinates.adjust_by(longitude=-1)
        elif coordinates.direction == CardinalPoint.EAST:
            return coordinates.adjust_by(latitude=1)
        elif coordinates.direction == CardinalPoint.WEST:
            return coordinates.adjust_by(latitude=-1)

    def backward(self, coordinate):
        if coordinate.direction == CardinalPoint.NORTH:
            return coordinate.adjust_by(longitude=-1)
        elif coordinate.direction == CardinalPoint.SOUTH:
            return coordinate.adjust_by(longitude=1)
        elif coordinate.direction == CardinalPoint.EAST:
            return coordinate.adjust_by(latitude=-1)
        elif coordinate.direction == CardinalPoint.WEST:
            return coordinate.adjust_by(latitude=1)

    def locate(self):
        return self.gps.current_coordinates()

    def turn_left(self, coordinate):
        direction = coordinate.direction.next_point_anti_clockwise()
        return coordinate.adjust_by(direction=direction)

    def turn_right(self, coordinate):
        direction = coordinate.direction.next_point_clockwise()
        return coordinate.adjust_by(direction=direction)
