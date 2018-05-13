from classes.point import Point
from classes.direction import Direction
from classes.cube import Cube
from time import time
from copy import deepcopy

class SnakeSolver:
    def __init__(self):
        self.ruled_out = 0
        self.previous_time = time() - 5
        self.longest_combo = []
        self.max_combo = 4 ** 46

    def solveSnake(self, snake_sections):
        self.recursivelySolveSnake(Cube(), list(reversed(snake_sections)), Direction.away, [])

    def recursivelySolveSnake(self, cube, snake_sections, direction, directions_so_far):
        current_time = time()
        if self.previous_time < current_time - 5:
            print(f"There are this many combinations possible: {self.max_combo}")
            print(f"We have ruled out this many combinations!: {self.ruled_out}")
            print(f"We need 46 twists")
            print(f"Best so far is {len(self.longest_combo)} twists: {self.longest_combo}")
            print("-----")
            self.previous_time = current_time

        if len(directions_so_far) >= len(self.longest_combo):
            self.longest_combo = list(directions_so_far)

        section_length = snake_sections.pop()
        directions_so_far.append(f"{direction.description()}({section_length})")

        for i in range(0, section_length):
            cube.fillDirection(direction)
            if not cube.isValid():
                self.ruled_out += (4 ** (46 - len(directions_so_far)))
                return

        if len(snake_sections) == 0:
            print()
            print("******************************************")
            print("*********** WE FOUND IT!!!!!!! ***********")
            print("******************************************")
            print()
            print(directions_so_far)
            exit(0)
        else:    
            for new_direction in direction.possibleNextDirections():
                self.recursivelySolveSnake(deepcopy(cube), list(snake_sections), new_direction, list(directions_so_far))