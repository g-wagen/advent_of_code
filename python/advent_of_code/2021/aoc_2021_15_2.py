from advent_of_code import helper
import numpy as np
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder


# GET THE DATA
data = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581",
]

data = helper.get_puzzle_input(d=15, y=2021)

# Make the data a numpy array
axis_0 = len(data)
axis_1 = len(data[0])
data = [int(x) for x in "".join(data)]
data = np.array(data).reshape((axis_0, axis_1))


# BUILD THE MAP
# Extend the map horizontally
full_map = data
new_chunk = data
for x in range(4):
    new_chunk = np.where(new_chunk + 1 > 9, 1, new_chunk + 1)
    full_map = np.hstack((full_map, new_chunk))

# Extend the map vertically
new_chunk = full_map
for y in range(4):
    new_chunk = np.where(new_chunk + 1 > 9, 1, new_chunk + 1)
    full_map = np.vstack((full_map, new_chunk))


# FIND THE LOWEST RISK PATH
grid = Grid(matrix=full_map)
start = grid.node(0, 0)
end = grid.node(full_map.shape[0] - 1, full_map.shape[1] - 1)

finder = DijkstraFinder()
path, runs = finder.find_path(start, end, grid)
print("operations:", runs, "path length:", len(path))


# COMPUTE THE RESULT
risk = 0
for coords in path[1:]:
    risk += full_map[coords[::-1]]

print(f"\nPuzzle answer: {risk}")
