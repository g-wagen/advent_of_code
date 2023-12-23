from aoc.helper import choose_puzzle_input, print_solution

year = 2023
day = 3

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


all_numeric_ranges = []
all_numeric_indices = []
gear_indices = []


# All 2d indices of gears
for y, line in enumerate(puzzle_input):
    numerics_indices = []
    for x, char in enumerate(line):
        if char == "*":
            gear_indices.append([y, x])
        elif char == ".":
            continue
        elif char.isnumeric():
            numerics_indices.append([y, x])
    all_numeric_indices.append(numerics_indices)

# slice indices of found numbers
for line in all_numeric_indices:
    numeric_range, beginnings, ends = [], [], []
    for i, item in enumerate(line):
        if i == 0:
            beginnings.append(item[1])
        elif i == len(line) - 1:
            ends.append(item[1])
        elif item[1] != line[i - 1][1] + 1:
            ends.append(line[i - 1][1])
            beginnings.append(item[1])

    for b, e in zip(beginnings, ends):
        numeric_range.append([b, e])

    all_numeric_ranges.append(numeric_range)


def has_numbers(
    puzzle,
    gear_y: int,
    gear_x: int,
    part_number_ranges: list,
) -> list[int]:
    left = gear_x - 1
    right = gear_x + 1
    above = gear_y - 1
    below = gear_y + 1

    part_numbers = []
    for rng in part_number_ranges[gear_y]:
        part_number = int(puzzle[gear_y][rng[0] : rng[1] + 1])
        if right == rng[0] or left == rng[1]:
            part_numbers.append(part_number)

    if above >= 0:
        for rng in part_number_ranges[above]:
            part_number = int(puzzle[above][rng[0] : rng[1] + 1])
            part_number_range = range(rng[0], rng[1] + 1)
            if (
                gear_x in part_number_range
                or right in part_number_range
                or left in part_number_range
            ):
                part_numbers.append(part_number)

    if below < len(puzzle):
        for rng in part_number_ranges[below]:
            part_number = int(puzzle[below][rng[0] : rng[1] + 1])
            part_number_range = range(rng[0], rng[1] + 1)
            if (
                gear_x in part_number_range
                or right in part_number_range
                or left in part_number_range
            ):
                part_numbers.append(part_number)

    return part_numbers


total = 0
for gear in gear_indices:
    part_nums = has_numbers(
        puzzle=puzzle_input,
        gear_y=gear[0],
        gear_x=gear[1],
        part_number_ranges=all_numeric_ranges,
    )

    if len(part_nums) == 2:
        total += part_nums[0] * part_nums[1]

print_solution(solution=total, y=year, d=day, part=2)
