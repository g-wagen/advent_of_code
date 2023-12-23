import re
from itertools import product
from re import Pattern

from aoc.helper import choose_puzzle_input, print_solution

year = 2023
day = 12

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


def generate_regex(seq_size: list[int]) -> Pattern:
    regex_prefix_and_suffix = r"\.*"
    regex = regex_prefix_and_suffix
    for i, subseq in enumerate(seq_size):
        regex += f"#{{{subseq}}}"
        if i != len(seq_size) - 1:
            regex += r"\.+"
    regex += regex_prefix_and_suffix
    return re.compile(pattern=regex)


def permutate(seq: str) -> list[str]:
    output = []
    positions = []

    possibilities = list(product(".#", repeat=seq.count("?")))

    for i, char in enumerate(seq):
        if char == "?":
            positions.append(i)

    for permutation in possibilities:
        out_str_list = [x for x in seq]

        for pchar, pos in zip(permutation, positions):
            out_str_list[pos] = pchar

        output.append("".join(out_str_list))

    return output


arrangements = []
for line in puzzle_input:
    possibilities = 0
    sequence, sequence_size = line.split(" ")
    sequence_size = [int(x) for x in sequence_size.split(",")]
    all_permutations = permutate(seq=sequence)

    valid_permurations = []
    for perm in all_permutations:
        if sequence_size == [len(x) for x in perm.split(".") if x]:
            valid_permurations.append(perm)

    the_pattern = generate_regex(seq_size=sequence_size)

    for permutation in valid_permurations:
        if re.match(pattern=the_pattern, string=permutation):
            possibilities += 1

    arrangements.append(possibilities)


print_solution(solution=sum(arrangements), y=year, d=day, part=1)
