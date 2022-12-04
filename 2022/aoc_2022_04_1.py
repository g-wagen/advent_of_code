from helper import get_puzzle_input, print_solution

puzzle_input = get_puzzle_input(y=2022, d=4)


class Assignment:
    elf1: set
    elf2: set


def calculate_range(elf_range: list) -> set:
    return {x for x in range(int(elf_range[0]), int(elf_range[-1]) + 1)}


def get_assignment(assignment_string: str) -> Assignment:
    assignment = Assignment()
    assignments = assignment_string.split(',')
    assignment.elf1 = calculate_range(assignments[0].split('-'))
    assignment.elf2 = calculate_range(assignments[1].split('-'))
    return assignment


def assignment_contains_other(first: set, second: set) -> bool:
    return first.issubset(second) or second.issubset(first)


redundant = 0

for item in puzzle_input:
    assignments = get_assignment(item)
    redundant += 1 if assignment_contains_other(assignments.elf1, assignments.elf2) else 0

if __name__ == '__main__':
    print_solution(redundant, 2022, 4, 1)
