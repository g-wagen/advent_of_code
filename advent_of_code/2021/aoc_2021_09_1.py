from advent_of_code import helper
import numpy as np

data = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]
data = helper.get_puzzle_input(d=9, y=2021)
axis_0 = len(data)
axis_1 = len(data[0])
data = [int(x) for x in "".join(data)]
data = np.array(data).reshape((axis_0, axis_1))

x_max = data.shape[1]
y_max = data.shape[0]

low_points = np.full(data.shape, np.nan)

for r, row in enumerate(data):
    for c, col in enumerate(row):
        current = data[r, c]
        neighbors = []
        if r - 1 > -1:
            neighbors.append(data[r - 1, c])
        if c - 1 > -1:
            neighbors.append(data[r, c - 1])
        if c + 1 < x_max:
            neighbors.append(data[r, c + 1])
        if r + 1 < y_max:
            neighbors.append(data[r + 1, c])

        if current < min(neighbors):
            low_points[r, c] = current


print("Low points\n", low_points[np.logical_not(np.isnan(low_points))], "\n")
risk_levels = low_points + 1

print(
    "Risk levels:\n", risk_levels[np.logical_not(np.isnan(risk_levels))], "\n"
)

risk_levels_sum = int(
    np.sum(risk_levels[np.logical_not(np.isnan(risk_levels))])
)
print(f"Puzzle answer: {risk_levels_sum}")
