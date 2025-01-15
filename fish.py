from vector import Vector2d

class Fish:
    def __init__(self, x: float, y: float):
        self.velo = Vector2d(0, 0)
        self.pos = Vector2d(x, y)

    def draw(self):
        pass

    def update(self):
        pass