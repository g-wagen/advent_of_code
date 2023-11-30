import helper
import numpy as np
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder


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

# data = helper.get_puzzle_input(d=15, y=2021)


axis_0 = len(data)
axis_1 = len(data[0])
data = [int(x) for x in "".join(data)]
data = np.array(data).reshape((axis_0, axis_1))
print(data)

grid = Grid(matrix=data)
start = grid.node(0, 0)
end = grid.node(data.shape[0] - 1, data.shape[1] - 1)

finder = DijkstraFinder()
path, runs = finder.find_path(start, end, grid)

# print('operations:', runs, 'path length:', len(path))
# print(grid.grid_str(path=path, start=start, end=end))

risk = 0
for coords in path[1:]:
    risk += data[coords[::-1]]

print(f"\nPuzzle answer: {risk}")
