class PositionBuilder:
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.orientation = None

    def facing_north(self):
        self.orientation = 'N'
        return self

    def move_north(self, units):
        self.y += units
        return self

    def build(self):
        return self.x, self.y, self.orientation


def initial_position():
    return PositionBuilder(0, 0)
