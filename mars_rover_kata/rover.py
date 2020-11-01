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
            coordinates = coordinates.update(latitude=coordinates.latitude + 1)
        if command == 'b':
            coordinates = coordinates.update(latitude=coordinates.latitude - 1)
        return coordinates

    def locate(self):
        return self.gps.current_coordinates()
