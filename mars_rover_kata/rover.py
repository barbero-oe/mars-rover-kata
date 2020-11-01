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
        if command == 'b':
            coordinates = coordinates.update(latitude=coordinates.latitude - 1)
        return coordinates

    def forward(self, coordinates):
        if coordinates.direction == Direction.NORTH:
            return coordinates.update(longitude=coordinates.longitude + 1)
        elif coordinates.direction == Direction.SOUTH:
            return coordinates.update(longitude=coordinates.longitude - 1)
        elif coordinates.direction == Direction.EAST:
            return coordinates.update(latitude=coordinates.latitude + 1)
        elif coordinates.direction == Direction.WEST:
            return coordinates.update(latitude=coordinates.latitude - 1)

    def locate(self):
        return self.gps.current_coordinates()
