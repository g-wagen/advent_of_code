from advent_of_code.helper import (
    print_solution,
    read_puzzle_input,
)

year = 2025
day = 9

puzzle_input = read_puzzle_input(input_path="aoc_2025_09_input.txt")
# puzzle_input = read_puzzle_input(input_path="aoc_2025_09_input_sample.txt")


def calc_area(point1: list[int], point2: list[int]) -> int:
    x = abs(point1[0] - point2[0]) + 1
    y = abs(point1[1] - point2[1]) + 1

    return x * y


def parse_input_to_coordinates(input) -> list[list[int]]:
    coords = []
    for line in input:
        coords.append([int(x) for x in line.split(",")])
    return coords


def d9p1() -> int:
    solution = 0

    coords = parse_input_to_coordinates(puzzle_input)

    for point1 in coords:
        for point2 in coords:
            area = calc_area(point1, point2)
            if area > solution:
                solution = area

    return solution


def d9p2() -> int:
    solution = 0

    coords = parse_input_to_coordinates(puzzle_input)

    grid = []

    max_x = max([x[0] for x in coords]) + 2
    max_y = max([y[1] for y in coords]) + 2

    for y in range(max_y):
        the_line = ["." for x in range(max_x)]
        grid.append(the_line)

    for coord in coords:
        grid[coord[1]][coord[0]] = "#"

    return solution

print_solution(solution=d9p1, y=year, d=day, part=1)


# print_solution(solution=d9p2, y=year, d=day, part=2)
