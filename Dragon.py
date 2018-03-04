class Dragon:

    def __init__(self):
        self.x = 0
        self.y = 0

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y
