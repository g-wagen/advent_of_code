from advent_of_code import helper
import numpy as np

data = """7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1

22 13 17 11  0
8  2 23  4 24
21  9 14 16  7
6 10  3 18  5
1 12 20 15 19

3 15  0  2 22
9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7"""

data = [x for x in data.split("\n")]
data = helper.get_puzzle_input(y=2021, d=4)

inputs = np.array([int(x) for x in data[0].split(",")])


grids = [x.strip().replace("  ", " ") for x in data[1:] if len(x) > 1]

for i, bi in enumerate(grids):
    numbers = [int(x) for x in bi.split()]
    grids[i] = numbers

dim = (int(len(grids) / 5), 5, 5)
grids = np.array(grids).reshape(dim)

stop = False
gridsum = 0

for num in inputs:
    grids = np.where(num == grids, np.nan, grids)
    for grid in grids:
        for row, col in zip(range(grid.shape[0]), range(grid.shape[1])):
            # horizontal
            bingo_row = np.isnan(grid[row]).all()
            # vertical
            bingo_col = np.isnan(grid[:, col]).all()

            if bingo_row or bingo_col:
                stop = True
                gridsum = int(np.sum(grid[np.logical_not(np.isnan(grid))]))

    if stop:
        print(f"Winning number: {num}")
        print(f"Board sum: {gridsum}")
        print(f"Winning number * board sum: {num * gridsum}")
        break
