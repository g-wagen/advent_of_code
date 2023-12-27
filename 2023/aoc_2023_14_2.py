import numpy as np
from tqdm import tqdm
from helper import choose_puzzle_input, print_solution


year = 2023
day = 14

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


def calculate_load(ground: list) -> int:
    load = []
    for y in range(len(ground)):
        for x in range(len(ground[0])):
            if ground[y][x] == "O":
                load.append(abs(y - len(ground)))
    return sum(load)


def move_rocks_reverse(line: list) -> list:
    out = []
    for split in "".join(line).split("#"):
        out.extend([*sorted(split, reverse=True), "#"])
    return out[:-1]


def move_rocks(line: list) -> list:
    out = []
    for split in "".join(line).split("#"):
        out.extend([*sorted(split, reverse=False), "#"])
    return out[:-1]


def spin_cycle(terrain):
    north = np.apply_along_axis(move_rocks_reverse, 0, terrain)
    west = np.apply_along_axis(move_rocks_reverse, 1, north)
    south = np.apply_along_axis(move_rocks, 0, west)
    return np.apply_along_axis(move_rocks, 1, south)


floor_with_rocks = np.array([[char for char in line] for line in puzzle_input])

# cycle repeats at 300 and 1000
cycles = 300

for i in tqdm(range(cycles)):
    floor_with_rocks = spin_cycle(floor_with_rocks)

load = calculate_load(ground=floor_with_rocks)
print_solution(solution=load, y=year, d=day, part=2)
