class Rover:
    def __init__(self, gps):
        self.gps = gps

    def instruct(self, commands):
        for command in commands:
            if command == 'f':
                current = self.gps.current_position()
                updated_position = (current[0], current[1] + 1, current[2])
                self.gps.update(updated_position)

    def locate(self):
        return self.gps.current_position()
