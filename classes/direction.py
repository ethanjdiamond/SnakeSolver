from enum import Enum

class Direction(Enum):
    right = 0
    left = 1
    up = 2
    down = 3
    away = 4
    toward = 5

    def possibleNextDirections(self):
        if self == Direction.right or self == Direction.left:
            return [Direction.away, Direction.toward, Direction.up, Direction.down]
        elif self == Direction.up or self == Direction.down:
            return [Direction.away, Direction.toward, Direction.left, Direction.right]
        elif self == Direction.away or self == Direction.toward:
            return [Direction.up, Direction.down, Direction.left, Direction.right]

    def opposite(self):
        if self == Direction.right:
            return Direction.left
        elif self == Direction.left:
            return Direction.right
        elif self == Direction.up:
            return Direction.down
        elif self == Direction.down:
            return Direction.up
        elif self == Direction.away:
            return Direction.toward
        elif self == Direction.toward:
            return Direction.away

    def description(self):
        if self == Direction.right:
            return "RIGHT"
        elif self == Direction.left:
            return "LEFT"
        elif self == Direction.up:
            return "UP"
        elif self == Direction.down:
            return "DOWN"
        elif self == Direction.away:
            return "AWAY"
        elif self == Direction.toward:
            return "TOWARD"