from mars_rover_kata.gps import Direction


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

    def forward(self, coordinates):
        if coordinates.direction == Direction.NORTH:
            return coordinates.adjust_by(longitude=1)
        elif coordinates.direction == Direction.SOUTH:
            return coordinates.adjust_by(longitude=-1)
        elif coordinates.direction == Direction.EAST:
            return coordinates.adjust_by(latitude=1)
        elif coordinates.direction == Direction.WEST:
            return coordinates.adjust_by(latitude=-1)

    def backward(self, coordinate):
        if coordinate.direction == Direction.NORTH:
            return coordinate.adjust_by(longitude=-1)
        elif coordinate.direction == Direction.SOUTH:
            return coordinate.adjust_by(longitude=1)
        elif coordinate.direction == Direction.EAST:
            return coordinate.adjust_by(latitude=-1)
        elif coordinate.direction == Direction.WEST:
            return coordinate.adjust_by(latitude=1)

    def locate(self):
        return self.gps.current_coordinates()
