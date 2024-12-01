from advent_of_code import helper
import matplotlib.pyplot as plt
import numpy as np


def plotting(x1, x2, y1, y2, size_x, size_y):
    """This is just for fun. Quite a lot of lines"""
    fig, ax = plt.subplots(1, 1, figsize=(size_x, size_y))
    ax.scatter(x1, y1)
    ax.scatter(x2, y2)
    # ax.xaxis.tick_top()
    for _x1, _y1, _x2, _y2 in zip(x1, y1, x2, y2):
        plt.plot((_x1, _x2), (_y1, _y2))

    # plt.axis([-.2, 9.2, 9.2, -.2])
    # plt.xticks(np.arange(0,10))
    # plt.yticks(np.arange(0,10))

    plt.show()


data = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]

data = helper.get_puzzle_input(d=5, y=2021)

data = [x.replace(" -> ", ",") for x in data]
data = np.array([int(x) for x in ",".join(data).split(",")]).reshape((
    len(data),
    4,
))

# X Coordinates
x1, x2 = data[:, 0], data[:, 2]
# Y Coordinates
y1, y2 = data[:, 1], data[:, 3]

# Generate the diagram template
field = np.full((np.max([y1, y2]) + 1, np.max([x1, x2]) + 1), 0)

for i, (__x1, __x2, __y1, __y2) in enumerate(zip(x1, x2, y1, y2)):
    # Generate points range between coordinates
    xrange = np.arange(__x1, __x2 + 1)
    yrange = np.arange(__y1, __y2 + 1)

    # The points ranges have to be generated in reverse in case the
    # first x or y coordinate pair is greater than the second one.
    # Afterwards the ranges have to be flipped to avoid using wrong coordinates.
    if __x1 > __x2:
        xrange = np.flip(np.arange(__x2, __x1 + 1))
    if __y1 > __y2:
        yrange = np.flip(np.arange(__y2, __y1 + 1))

    # X and Y are flipped here to get an accurate output.
    # This is weird but works for now :-D

    # Draw horizontal lines
    if len(xrange) > len(yrange):
        for x in xrange:
            field[yrange[0], x] += 1

    # Draw diagonals
    elif len(xrange) == len(yrange):
        for x, y in zip(xrange, yrange):
            field[y, x] += 1

    # Draw vertical lines
    elif len(xrange) < len(yrange):
        for y in yrange:
            field[y, xrange[0]] += 1

# Count the overlaps
overlaps = len(field[field > 1])
print(f"Overlapping count: {overlaps}")
