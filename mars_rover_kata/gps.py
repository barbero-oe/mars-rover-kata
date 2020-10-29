class GPS:
    def __init__(self, position):
        self.position = position

    def current_position(self):
        return self.position

    def update(self, position):
        self.position = position
