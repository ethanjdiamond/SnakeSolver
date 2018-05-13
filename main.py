from classes.snake_brute_force_solver import SnakeBruteForceSolver
from classes.snake_other_solver import SnakeOtherSolver

snake_sections = [2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 3, 1, 1, 1, 3, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 3, 1, 1, 2, 1, 2]

var = input("Which way do you want to solve it? \n1. Brute Force\n2. ????????\n")
if str(var) == "1":
	snake_solver = SnakeBruteForceSolver()
elif str(var) == "2":
	snake_solver = SnakeOtherSolver()
else:
	print("That's not an option, dummy")
	exit(1)

print("")

snake_solver.solveSnake(snake_sections)