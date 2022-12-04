import numpy

import helper
import matplotlib.pyplot as plt
import numpy as np


def plotting(x1, x2, y1, y2, size_x, size_y):
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
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2',
]

data = helper.get_puzzle_input(d=5, y=2021)

data = [x.replace(' -> ', ',') for x in data]
data = np.array([int(x) for x in ','.join(data).split(',')])\
    .reshape((len(data), 4))

x1, x2 = data[:, 0], data[:, 2]
y1, y2 = data[:, 1], data[:, 3]

horiz = x1 == x2
vert = y1 == y2

keep = []
for i, (h, v) in enumerate(zip(horiz, vert)):
    if np.any([h, v]):
        keep.append(i)

x1, x2 = x1[keep], x2[keep]
y1, y2 = y1[keep], y2[keep]

# Generate the diagram template
field = np.full((np.max([y1, y2])+1, np.max([x1, x2])+1), 0)

# Populate the field
for i, (__x1, __x2, __y1, __y2) in enumerate(zip(x1, x2, y1, y2)):
    xrange = np.arange(__x2, __x1+1) if __x1 > __x2 else np.arange(__x1, __x2 + 1)
    yrange = np.arange(__y2, __y1+1) if __y1 > __y2 else np.arange(__y1, __y2 + 1)

    if len(xrange) > len(yrange):
        for x in xrange:
            field[yrange[0], x] += 1
    else:
        for y in yrange:
            field[y, xrange[0]] += 1

# Count the overlaps
overlaps = len(field[field > 1])
print(f'Overlapping count: {overlaps}')