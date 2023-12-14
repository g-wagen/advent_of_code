from aoc_2022_04_1 import puzzle_input, get_assignment
from helper import print_solution


def assignment_contains_other_partially(first: set, second: set) -> bool:
    return True if set.intersection(first, second) else False


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

if __name__ == "__main__":
    print_solution(redundant, 2022, 4, 2)
