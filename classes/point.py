from classes.direction import Direction

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y and self.z == point.z

    def zero():
        return Point(0, 0, 0)

    def shift(self, direction):
        if direction == Direction.right:
            self.x += 1
        elif direction == Direction.left:
            self.x -= 1
        elif direction == Direction.up:
            self.y += 1
        elif direction == Direction.down:
            self.y -= 1
        elif direction == Direction.away:
            self.z += 1
        elif direction == Direction.toward:
            self.z -= 1

    def description(self):
        return f"({self.x}, {self.y}, {self.z})"