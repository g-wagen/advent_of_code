from helper import choose_puzzle_input, print_solution

year = 2023
day = 15

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


def hash_alg(sequence: str) -> int:
    out = 0
    for item in sequence:
        out += ord(item)
        out *= 17
        out = out % 256
    return out


values = [hash_alg(wtf) for wtf in puzzle_input[0].split(",")]

print_solution(solution=sum(values), y=year, d=day, part=1)
