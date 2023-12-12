from helper import choose_puzzle_input, print_solution
import math
import json

year = 2023
day = 11

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)

vertical_expansion = []

# vertical expansion
for line in puzzle_input:
    vertical_expansion.append(line)
    if line.find("#") < 0:
        vertical_expansion.append(line)


vertical_galaxy_counter = []
for i, column in enumerate(vertical_expansion[0]):
    galaxy_counter = 0
    for row in range(len(vertical_expansion)):
        if vertical_expansion[row][i] == "#":
            galaxy_counter += 1
    vertical_galaxy_counter.append(galaxy_counter)


horizontal_expansion = []
for row in vertical_expansion:
    expanded_horizontal_row = ""
    for x, column in enumerate(row):
        expanded_horizontal_row += column
        if vertical_galaxy_counter[x] == 0:
            expanded_horizontal_row += column
    horizontal_expansion.append(expanded_horizontal_row)


galaxy_coordinates = []
for y, row in enumerate(horizontal_expansion):
    for x, column in enumerate(row):
        if column == "#":
            galaxy_coordinates.append([y, x])


pairs = []
for i, coord in enumerate(galaxy_coordinates):
    for coord2 in galaxy_coordinates[i + 1 :]:
        pairs.append([coord, coord2])


def galaxy_distance(g1, g2):
    xdistance = abs(g2[1] - g1[1])
    ydistance = abs(g2[0] - g1[0])

    return xdistance + ydistance


total = 0
for pair in pairs:
    total += galaxy_distance(pair[1], pair[0])

print_solution(solution=total, y=year, d=day, part=1)
