from typing import Callable

from helper import choose_puzzle_input, print_solution

year = 2023
day = 9

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


def diff_line(sequence: list[int]) -> list[int]:
    newline = []
    for i, number in enumerate(sequence):
        try:
            newline.append(sequence[i + 1] - number)
        except IndexError:
            pass
    return newline


def same_diff(sequence: list[int]) -> bool:
    return True if len(set(sequence)) == 1 else False


def next_in_series(
    numbers: list[int], step_diff_func: Callable, same_steps_func: Callable
) -> list[int]:
    temp_sequence = []
    out_sequence = numbers
    while True:
        if not temp_sequence:
            temp_sequence.append(step_diff_func(number_sequence))
        elif same_steps_func(temp_sequence[-1]):
            end = numbers[-1]
            for sequence in temp_sequence:
                end += sequence[-1]
            out_sequence.append(end)
            break
        else:
            temp_sequence.append(step_diff_func(temp_sequence[-1]))
    return out_sequence


next_value = []
for line in puzzle_input:
    sequences = []
    number_sequence = [int(x) for x in line.split()]

    next_value.append(
        next_in_series(
            numbers=number_sequence,
            step_diff_func=diff_line,
            same_steps_func=same_diff,
        )[-1]
    )

print_solution(solution=sum(next_value), y=year, d=day, part=1)


next_value = []
for line in puzzle_input:
    sequences = []
    number_sequence = [int(x) for x in line.split()][::-1]

    next_value.append(
        next_in_series(
            numbers=number_sequence,
            step_diff_func=diff_line,
            same_steps_func=same_diff,
        )[-1]
    )

print_solution(solution=sum(next_value), y=year, d=day, part=2)
