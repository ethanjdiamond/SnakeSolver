from classes.direction import Direction
from classes.point import Point
from copy import deepcopy

class Cube:
    def __init__(self):
        # All points with a piece of the snake in them in them. We assume anything else is empty.
        self.current_point = Point.zero()
        self.filled_points = set()
        self.cube_dimension = 4
        self.is_valid = True

    def pointIsValid(self, point):
        x_is_valid = point.x >= 0 and point.x < self.cube_dimension
        y_is_valid = point.y >= 0 and point.y < self.cube_dimension
        z_is_valid = point.z >= 0 and point.z < self.cube_dimension
        return x_is_valid and y_is_valid and z_is_valid

    def isValid(self):
        return self.is_valid

    def isEmpty(self):
        return len(self.filled_points) == 0

    def pointIsFilled(self, point):
        return point in self.filled_points

    def fillPoint(self, point):
        if point in self.filled_points or not self.pointIsValid(point):
            self.is_valid = False
        self.filled_points.add(deepcopy(point))

    def fillDirection(self, direction):
        # If it's the first insert, just populate (0, 0, 0) and ignore everything else
        if self.isEmpty():
            self.fillPoint(self.current_point)
        else:
            self.current_point.shift(direction)
            if not self.pointIsValid(self.current_point):
                self.shift(direction.opposite())
            self.fillPoint(self.current_point)

    def shift(self, direction):
        old_filled_points = self.filled_points
        self.filled_points = set()
        self.current_point.shift(direction)
        for point in old_filled_points:
            point.shift(direction)
            self.fillPoint(point)

    def description(self):
        return ", ".join(list(map(lambda x: x.description(), list(self.filled_points))))

    def drawing(self):
        description = "---"
        for z in range(self.cube_dimension):
            columns = []
            for x in range(self.cube_dimension):
                rows = []
                for y in range(self.cube_dimension):
                    rows.append("1" if Point(x, y, z) in self.filled_points else "0")
                columns.append(", ".join(rows))
            description += "\n".join(columns) + "\n---\n"
        return description