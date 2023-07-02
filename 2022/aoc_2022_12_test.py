from helper import get_puzzle_input, print_solution
import numpy as np
from string import ascii_lowercase
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder, AStarFinder

puzzle_input = get_puzzle_input(y=2022, d=12)
with open('aoc_2022_12_inputsample.txt', 'r') as f:
    puzzle_input = f.read().splitlines()

lowercase = {'S': 0}
lowercase.update({l: i+1 for l, i in zip(ascii_lowercase, range(len(ascii_lowercase)))})
lowercase.update({'E': len(ascii_lowercase)+1})

axis_0 = len(puzzle_input)
axis_1 = len(puzzle_input[0])
data = [lowercase[x] for x in ''.join(puzzle_input)]
data = np.array(data).reshape((axis_0, axis_1))

min_value = np.min(data)
max_value = np.max(data)

start_coords = np.array(np.where(data == np.min(data))).flatten()
end_coords = np.array(np.where(data == np.max(data))).flatten()

# print(start_coords, end_coords)

grid = Grid(matrix=data)
start = grid.node(start_coords[1], start_coords[0])
end = grid.node(end_coords[1], end_coords[0])

finder = DijkstraFinder()
path, runs = finder.find_path(start, end, grid)

# print(path)
# print(runs)
# print(data)
print(grid.grid_str(path=path, start=start, end=end))
the_way = np.full([*data.shape], 0)

for c, crds in enumerate(path):
    the_way[crds[::-1]] = data[crds[::-1]]

print(the_way)
print(data)
print_solution('solution', y=2022, d=12, part=1)
