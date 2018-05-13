from classes.point import Point
from classes.direction import Direction
from copy import deepcopy

# shifted works
point = Point(1, 1, 1)
point.shift(Direction.right)
assert point == Point(2, 1, 1)

point = Point(1, 1, 1)
point.shift(Direction.left)
assert point == Point(0, 1, 1)

point = Point(1, 1, 1)
point.shift(Direction.up)
assert point == Point(1, 2, 1)

point = Point(1, 1, 1)
point.shift(Direction.down)
assert point == Point(1, 0, 1)

point = Point(1, 1, 1)
point.shift(Direction.away)
assert point == Point(1, 1, 2)

point = Point(1, 1, 1)
point.shift(Direction.toward)
assert point == Point(1, 1, 0)

# copy works
point_a = Point(1, 1, 1)
point_b = deepcopy(point_a)
point_b.x = 2
assert(point_a == Point(1, 1, 1))

point_a = Point(1, 1, 1)
point_b = point_a
point_b.x = 2
assert(point_a == Point(2, 1, 1))

print("SUCCESS")