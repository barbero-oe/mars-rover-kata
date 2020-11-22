from mars_rover_kata.cardinal_point import CardinalPoint


class Navigation:
    def __init__(self):
        self.backwards = {CardinalPoint.NORTH: (0, -1),
                          CardinalPoint.SOUTH: (0, 1),
                          CardinalPoint.EAST: (-1, 0),
                          CardinalPoint.WEST: (1, 0)}
        self.forward = {CardinalPoint.NORTH: (0, 1),
                        CardinalPoint.SOUTH: (0, -1),
                        CardinalPoint.EAST: (1, 0),
                        CardinalPoint.WEST: (-1, 0)}

    def move_backwards(self, direction):
        return self.backwards.get(direction)

    def move_forward(self, direction):
        return self.forward.get(direction)
