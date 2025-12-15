from advent_of_code.helper import (
    print_solution,
    read_puzzle_input,
)

year = 2025
day = 9

puzzle_input = read_puzzle_input(input_path="aoc_2025_09_input.txt")
# puzzle_input = read_puzzle_input(input_path="aoc_2025_09_input_sample.txt")

coords = []
for line in puzzle_input:
    coords.append([int(x) for x in line.split(",")])

def calc_area(point1: list[int], point2: list[int]) -> int:
    x = abs(point1[0] - point2[0]) + 1
    y = abs(point1[1] - point2[1]) + 1

    return x * y


def d9p1() -> int:
    solution = 0

    for point1 in coords:
        for point2 in coords:
            area = calc_area(point1, point2)
            if area > solution:
                solution = area

    return solution


def d9p2() -> int:
    solution = 0

    for line in puzzle_input:
        ...

    return solution


print_solution(solution=d9p1(), y=year, d=day, part=1)

print_solution(solution=d9p2(), y=year, d=day, part=2)
