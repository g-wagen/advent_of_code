from advent_of_code import helper
import numpy as np

data = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]

data = helper.get_puzzle_input(d=11, y=2021)

ax_0 = len(data)
ax_1 = len(data[0])
data = [int(x) for x in "".join(data)]
data = np.array(data).reshape((ax_0, ax_1)).astype("float")
data = np.pad(data, 1, mode="constant", constant_values=np.NINF)


def flashing_dumbos(arr):
    flashes = np.count_nonzero(arr > 9)
    flash_y, flash_x = np.where(arr > 9)
    # Change flashed into NAN.
    # This way the value won't change if multiplied or added.
    arr = np.where(arr > 9, np.nan, arr)

    for y, x in zip(flash_y, flash_x):
        arr[y - 1 : y + 2, x - 1 : x + 2] += 1
    return arr, flashes


def fix_nan(arr):
    return np.where(np.isnan(arr), 0, arr)


steps = 0

while not np.all(data[1:-1, 1:-1].astype("int") == 0):
    data += 1
    steps += 1
    data, flashes = flashing_dumbos(data)
    while flashes > 0:
        # total_flashes += flashes
        data, flashes = flashing_dumbos(data)
    data = fix_nan(data)

print(f"Puzzle answer is: {steps}")
