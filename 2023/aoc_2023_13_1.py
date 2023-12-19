from typing import Union
from helper import choose_puzzle_input, print_solution

year = 2023
day = 13

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


patterns = {}
pattern_counter = 0
for p in puzzle_input:
    if p:
        if pattern_counter not in patterns:
            patterns[pattern_counter] = []
        patterns[pattern_counter].append(p)
    else:
        pattern_counter += 1


def find_mirrors(pattern: list[str]) -> list[int]:
    mirror_planes = []
    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i + 1]:
            mirror_planes.append(i)
    return mirror_planes


def verify_mirror_planes(
    pattern: list[str], mirror_planes: list[int]
) -> Union[int, None]:
    for mp in mirror_planes:
        left_side = pattern[: mp + 1][::-1]
        right_side = pattern[mp + 1 :]
        short, long = sorted([left_side, right_side], key=lambda x: len(x))

        is_subset = []
        for s, l in zip(short, long):
            is_subset.append(True if s == l else False)

        if all(is_subset):
            return mp


def rotate_pattern(pattern: list[str]) -> list[str]:
    return ["".join(item) for item in list(zip(*pattern[::-1]))]


total = 0

for pattern in patterns.values():
    potential_horizontal_reflections = find_mirrors(pattern)
    horizontal_reflection = verify_mirror_planes(
        pattern, potential_horizontal_reflections
    )

    if horizontal_reflection in range(len(pattern)):
        total += 100 * (horizontal_reflection + 1)
    else:
        rotated_pattern = rotate_pattern(pattern)
        potential_vertical_reflections = find_mirrors(rotated_pattern)
        vertical_reflection = verify_mirror_planes(
            rotated_pattern, potential_vertical_reflections
        )
        total += vertical_reflection + 1


print_solution(solution=total, y=year, d=day, part=1)
