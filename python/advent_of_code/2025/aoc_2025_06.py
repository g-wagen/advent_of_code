from advent_of_code.helper import print_solution, read_puzzle_input

year = 2025
day = 6

puzzle_input = read_puzzle_input(input_path="aoc_2025_06_input.txt")


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

    grid = []

    for r, row in enumerate(puzzle_input):
        oneline = []
        for c, column in enumerate(row):
            oneline.append(column)
        grid.append(oneline)

    rotated = rotate_2d(grid)

    last_operation = ""
    last_numbers = []

    # add an empty row add the end
    rotated.append([" " * len(rotated[0])])

    for i, line in enumerate(rotated):
        if line[0] in ["+", "*"]:
            last_operation = line[0]

        line_as_string = "".join([n for n in reversed(line[1:])])

        try:
            last_numbers.append(int(line_as_string))
        except ValueError:
            if last_operation == "+":
                for number in last_numbers:
                    solution += number

            if last_operation == "*":
                mult = 1
                for number in last_numbers:
                    mult *= number
                solution += mult

            last_numbers = []

    return solution


print_solution(solution=d6p1(), y=year, d=day, part=1)

print_solution(solution=d6p2(), y=year, d=day, part=2)
