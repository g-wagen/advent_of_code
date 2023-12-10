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


next_value = []

for line in puzzle_input:
    sequences = []
    number_sequence = [int(x) for x in line.split()]
    while True:
        if not sequences:
            sequences.append(diff_line(number_sequence))
        elif same_diff(sequences[-1]):
            end = number_sequence[-1]
            for sequence in sequences:
                end += sequence[-1]
            next_value.append(end)
            break
        else:
            sequences.append(diff_line(sequences[-1]))


print_solution(solution=sum(next_value), y=year, d=day, part=1)
