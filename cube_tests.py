from classes.point import Point
from classes.direction import Direction
from classes.cube import Cube
from copy import deepcopy

# Fill works
cube = Cube()
cube.fillPoint(Point(1, 1, 1))
cube.fillPoint(Point(2, 2, 2))
cube.shift(Direction.right)
assert(cube.filled_points == set([Point(2, 1, 1), Point(3, 2, 2)]))

# isValid works
cube = Cube()
assert(cube.isValid())
cube.fillPoint(Point(4, 0, 0))
assert(not cube.isValid())

# pointIsValid works
cube = Cube()
assert(cube.pointIsValid(Point(0, 0, 0)))
assert(not cube.pointIsValid(Point(4, 0, 0)))
assert(not cube.pointIsValid(Point(0, 0, -1)))

# pointIsFilled works
cube = Cube()
cube.fillPoint(Point(1, 1, 1))
assert(cube.pointIsFilled(Point(1, 1, 1)))
assert(not cube.pointIsFilled(Point(0, 0, 0)))

# fillDirection works with first insert
cube = Cube()
cube.fillDirection(Direction.right)
assert(cube.current_point == Point(0, 0, 0))
assert(cube.filled_points == set([Point(0, 0, 0)]))

# fillDirection works without shift
cube = Cube()
cube.fillDirection(Direction.right)
cube.fillDirection(Direction.right)
assert(cube.current_point == Point(1, 0, 0))
assert(cube.filled_points == set([Point(0, 0, 0), Point(1, 0, 0)]))

# fillDirection works with basic shift
cube = Cube()
cube.fillDirection(Direction.away)
cube.fillDirection(Direction.left)
assert(cube.isValid())
assert(cube.filled_points == set([Point(1, 0, 0), Point(0, 0, 0)]))

# fillDirection works over time...
cube = Cube()
cube.fillDirection(Direction.right)
cube.fillDirection(Direction.right)
cube.fillDirection(Direction.right)
cube.fillDirection(Direction.right)
assert(cube.isValid())
assert(cube.current_point == Point(3, 0, 0))
assert(cube.filled_points == set([Point(0, 0, 0), Point(1, 0, 0), Point(2, 0, 0), Point(3, 0, 0)]))

# but fails when it goes over the side
cube.fillDirection(Direction.right)
assert(not cube.isValid())

# fillDirection works in multiple directions...
cube = Cube()
cube.fillDirection(Direction.away)
cube.fillDirection(Direction.right)
cube.fillDirection(Direction.up)
cube.fillDirection(Direction.left)
assert(cube.isValid())
assert(cube.current_point == Point(0, 1, 0))
assert(cube.filled_points == set([Point(0, 0, 0), Point(1, 0, 0), Point(1, 1, 0), Point(0, 1, 0)]))

# but fails when it runs into itself
cube.fillDirection(Direction.down)
assert(not cube.isValid())

# copy works
cube = Cube()
cube_2 = cube
cube_2.fillPoint(Point(1, 1, 1))
assert(cube.pointIsFilled(Point(1, 1, 1)))

cube = Cube()
cube_2 = deepcopy(cube)
cube_2.fillPoint(Point(1, 1, 1))
assert(not cube.pointIsFilled(Point(1, 1, 1)))

print("SUCCESS")