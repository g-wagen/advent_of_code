import numpy as np
from collections import deque

from helper import choose_puzzle_input

# puzzle_input = [
#     "Sabqponm",
#     "abcryxxl",
#     "accszExk",
#     "acctuvwj",
#     "abdefghi"
# ]

puzzle_input = choose_puzzle_input(
    y=2022, d=12, sample_input_path="aoc_2022_12_inputsample.txt"
)
# puzzle_input = choose_puzzle_input(y=2022, d=12)
character = ord("a")
print(puzzle_input)
data = []
for line in puzzle_input:
    new_line = []
    for char in line:
        if char.islower():
            new_line.append(1 + ord(char) - character)
        if char == "S":
            new_line.append(0)
        if char == "E":
            new_line.append(27)
    data.append(new_line)


print(data)


def find_paths_recursive(grid, current_path=[(0, 0)], solutions=[]):
    n = len(grid)
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    last_cell = current_path[-1]

    for x, y in dirs:
        new_i = last_cell[0] + x
        new_j = last_cell[1] + y

        # Check if new cell is in grid
        if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n:
            continue

        # Check if new cell is already in path
        if (new_i, new_j) in current_path:
            continue

        # Add cell to current path
        current_path_copy = current_path.copy()
        current_path_copy.append((new_i, new_j))

        if new_i == n - 1 and new_j == n - 1:
            continue

        # Check if new cell has bigger value than last
        if grid[new_i][new_j] > grid[last_cell[0]][last_cell[1]]:
            solutions.append(current_path_copy)

        # Create new current_path array for every direction
        find_paths_recursive(grid, current_path_copy, solutions)

    return solutions


solutions = find_paths_recursive(data)

lenghts = set()
for solution in solutions:
    lenghts.add(len(solution))

print(min(lenghts))
