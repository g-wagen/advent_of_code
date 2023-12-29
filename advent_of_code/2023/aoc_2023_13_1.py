from advent_of_code.helper import choose_puzzle_input, print_solution

year = 2023
day = 13

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)

temp = "\n".join(puzzle_input)
patterns = [
    [[0 if char == "." else 1 for char in line] for line in pattern.split("\n")]
    for pattern in temp.split("\n\n")
]


def horizontal_reflection(pattern: list[list[int]]) -> int:
    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i + 1]:
            left_side = pattern[: i + 1][::-1]
            right_side = pattern[i + 1 :]
            short, long = sorted([left_side, right_side], key=lambda x: len(x))
            if long[: len(short)] == short:
                return i + 1
    return -1


def rotate_2d(pattern: list[list[int]]) -> list[list[int]]:
    return [list(line) for line in list(zip(*pattern[::-1]))]


def vertical_reflection(pattern: list[list[int]]) -> int:
    return horizontal_reflection(pattern=rotate_2d(pattern=pattern))


def score_horizontal(h: int) -> int:
    return h * 100


def score_vertical(v: int) -> int:
    return v


total = 0

for i, pattern in enumerate(patterns):
    horizontal_line = horizontal_reflection(pattern)
    vertical_line = vertical_reflection(pattern)
    if horizontal_line > -1:
        total += score_horizontal(horizontal_line)
    else:
        total += score_vertical(vertical_line)

print_solution(solution=total, y=year, d=day, part=1)