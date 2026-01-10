from advent_of_code.helper import read_puzzle_input, print_solution

year = 2023
day = 11

puzzle_input = read_puzzle_input(input_path=f"aoc_{year}_{day:02d}_input.txt")


def calculate_galaxy_distance(g1, g2):
    x_distance = abs(g2[1] - g1[1])
    y_distance = abs(g2[0] - g1[0])
    return x_distance + y_distance

def increment_number_with_gaps(
    gaps: list[int], number: int, increment_by: int
) -> int:
    new_number = number
    for gap in gaps:
        if number > gap:
            new_number += increment_by
    return new_number

def y2023d11p1():
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

    total = 0
    for pair in pairs:
        total += calculate_galaxy_distance(pair[1], pair[0])

    return total

def y2023d11p2():
    universe_expansion = 1000000 - 1

    galaxy_coordinates_past = []
    for y, row in enumerate(puzzle_input):
        for x, column in enumerate(row):
            if column == "#":
                galaxy_coordinates_past.append((y, x))

    y_range = len(puzzle_input)
    x_range = len(puzzle_input[0])

    existing_y = {gc[0] for gc in galaxy_coordinates_past}
    existing_x = {gc[1] for gc in galaxy_coordinates_past}

    missing_y = sorted(list(set(range(y_range)).difference(existing_y)))
    missing_x = sorted(list(set(range(x_range)).difference(existing_x)))

    galaxy_coordinates_now = []
    for gc in galaxy_coordinates_past:
        y = gc[0]
        x = gc[1]
        new_y = increment_number_with_gaps(
            gaps=missing_y, number=y, increment_by=universe_expansion
        )
        new_x = increment_number_with_gaps(
            gaps=missing_x, number=x, increment_by=universe_expansion
        )
        galaxy_coordinates_now.append((new_y, new_x))

    pairs = []
    for i, coord in enumerate(galaxy_coordinates_now):
        for coord2 in galaxy_coordinates_now[i + 1:]:
            pairs.append([coord, coord2])

    total_distance = 0
    for pair in pairs:
        total_distance += calculate_galaxy_distance(pair[1], pair[0])

    return total_distance



print_solution(solution=y2023d11p1, y=year, d=day, part=1)

print_solution(solution=y2023d11p2, y=year, d=day, part=2)