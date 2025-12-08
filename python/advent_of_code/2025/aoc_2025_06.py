from advent_of_code.helper import print_solution, read_puzzle_input

year = 2025
day = 6

# puzzle_input = read_puzzle_input(input_path="aoc_2025_06_input.txt")


puzzle_input = read_puzzle_input(input_path="aoc_2025_06_input_sample.txt")


def rotate_2d(pattern: list[list[str]]) -> list[list[str]]:
    return [list(line) for line in list(zip(*pattern[::-1]))]


def d6p1() -> int:
    solution = 0
    lines = []

    for line in puzzle_input:
        lines.append(line.split())

    rotated = rotate_2d(lines)

    for equation in rotated:
        if equation[0] == "+":
            for item in equation[1:]:
                solution += int(item)

        elif equation[0] == "*":
            multi = 1
            for item in equation[1:]:
                multi *= int(item)
            solution += multi

    return solution


def d6p2() -> int:
    solution = 0

    return solution


print_solution(solution=d6p1(), y=year, d=day, part=1)

print_solution(solution=d6p2(), y=year, d=day, part=2)
