from advent_of_code.helper import choose_puzzle_input, print_solution, read_puzzle_input

year = 2025
day = 1

puzzle_input = read_puzzle_input(input_path="aoc_2025_01_input.txt")

min_value = 0
max_value = 99

ze_array = [x for x in range(100)]

def interpret_value(value: str) -> int:
    return int(value[1:]) if value[0] == "R" else -int(value[1:])

def d1p1() -> int:
    position = 50
    new_position = position
    solution = 0

    for line in puzzle_input:
        new_position += interpret_value(line)
        current_value = ze_array[new_position % (max_value + 1)]

        solution += 1 if current_value == 0 else 0

    return solution


def d1p2() -> int:
    position = 50
    new_position = position
    solution = 0

    for line in puzzle_input:
        clicks = int(line[1:])

        for i in range(clicks):
            if line[0] == "R":
                new_position += 1

            elif line[0] == "L":
                new_position -= 1

            current_value = ze_array[new_position % (max_value + 1)]
            solution += 1 if current_value == 0 else 0

    return solution


print_solution(solution=d1p1(), y=year, d=day, part=1)

print_solution(solution=d1p2(), y=year, d=day, part=2)
