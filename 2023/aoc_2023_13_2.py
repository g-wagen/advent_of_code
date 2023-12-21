from typing import Callable, Optional

from helper import choose_puzzle_input, print_solution

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


def horizontal_reflection(
    pattern: list[list[int]], old_reflection: Optional[int] = None
) -> int:
    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i + 1]:
            left_side = pattern[: i + 1][::-1]
            right_side = pattern[i + 1 :]
            short, long = sorted([left_side, right_side], key=lambda x: len(x))
            if long[: len(short)] == short:
                new_reflection = i + 1
                if old_reflection is None or old_reflection != new_reflection:
                    return new_reflection
    return -1


def rotate_2d(pattern: list[list[int]]) -> list[list[int]]:
    return [list(line) for line in list(zip(*pattern[::-1]))]


def vertical_reflection(
    pattern: list[list[int]], old_reflection: Optional[int] = None
) -> int:
    return horizontal_reflection(
        pattern=rotate_2d(pattern=pattern), old_reflection=old_reflection
    )


def score_horizontal(h: int) -> int:
    return h * 100


def score_vertical(v: int) -> int:
    return v


def spot_clean(pattern: list[list[int]], y: int, x: int) -> list[list[int]]:
    cleaned = [line.copy() for line in pattern]
    cleaned[y][x] = abs(cleaned[y][x] - 1)
    return cleaned


def smudge_reflection(
    pattern: list[list[int]], reflection_function: Callable, old_reflection: int
) -> int:
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            cleaned = spot_clean(pattern=pattern, y=y, x=x)
            new_reflection = reflection_function(
                pattern=cleaned, old_reflection=old_reflection
            )
            if new_reflection > -1:
                return new_reflection
    return -1


total = 0

for pattern in patterns:
    old_horizontal_line = horizontal_reflection(pattern=pattern)
    old_vertical_line = vertical_reflection(pattern=pattern)

    horizontal_line = smudge_reflection(
        pattern=pattern,
        reflection_function=horizontal_reflection,
        old_reflection=old_horizontal_line,
    )
    vertical_line = smudge_reflection(
        pattern=pattern,
        reflection_function=vertical_reflection,
        old_reflection=old_vertical_line,
    )

    if horizontal_line > -1:
        total += score_horizontal(horizontal_line)
    else:
        total += score_vertical(vertical_line)

print_solution(solution=total, y=year, d=day, part=2)
