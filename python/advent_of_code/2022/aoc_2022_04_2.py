from aoc_2022_04_1 import get_assignment, puzzle_input

from advent_of_code.helper import print_solution


def assignment_contains_other_partially(first: set, second: set) -> bool:
    return True if set.intersection(first, second) else False


def d4p2():
    redundant = 0

    for item in puzzle_input:
        assignments = get_assignment(item)
        redundant += (
            1
            if assignment_contains_other_partially(
                assignments.elf1, assignments.elf2
            )
            else 0
        )
    return redundant


print_solution(d4p2, 2022, 4, 2)
