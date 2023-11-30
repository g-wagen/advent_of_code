import helper
import numpy as np
from scipy import ndimage

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

areas, num_areas = ndimage.label(data < 9)
nines_count = data[data == 9].shape[0]
size = np.bincount(areas.flatten())
size = np.delete(size, np.where(size == nines_count))
sort_by_size = sorted(size)[::-1]
biggest_three = sort_by_size[:3]

print(f"Puzzle answer: {np.prod(biggest_three)}")
