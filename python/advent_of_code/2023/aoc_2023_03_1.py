from advent_of_code.helper import choose_puzzle_input, print_solution

year = 2023
day = 3

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


schematic = []
all_numeric_ranges = []
all_numeric_indices = []
part_number_chars = ""
total = []


# All 2d indices of numeric characters
for y, line in enumerate(puzzle_input):
    numerics_indices = []
    for x, char in enumerate(line):
        if char.isnumeric():
            numerics_indices.append([y, x])
        elif char == ".":
            continue
        elif char not in part_number_chars:
            part_number_chars += char
    all_numeric_indices.append(numerics_indices)

# slice indices of found numbers
for line in all_numeric_indices:
    numeric_range, beginnings, ends = [], [], []
    for i, item in enumerate(line):
        if i == 0:
            beginnings.append(item[1])
        elif i == len(line) - 1:
            ends.append(item[1])
        elif item[1] != line[i - 1][1] + 1:
            ends.append(line[i - 1][1])
            beginnings.append(item[1])

    for b, e in zip(beginnings, ends):
        numeric_range.append([b, e])

    all_numeric_ranges.append(numeric_range)


def has_symbols(puzzle, sym: str, y: int, x1: int, x2: int) -> bool:
    left = x1 - 1
    right = x2 + 1
    above = y - 1
    below = y + 1

    chars, has_it = "", []

    # links
    chars += puzzle[y][left] if left >= 0 else ""
    # rechts
    chars += puzzle[y][right] if right < len(puzzle[y]) else ""
    # oben links
    chars += puzzle[above][left] if above >= 0 and left >= 0 else ""
    # oben rechts
    chars += (
        puzzle[above][right] if above >= 0 and right < len(puzzle[y]) else ""
    )
    # unten links
    chars += puzzle[below][left] if below < len(puzzle) and left >= 0 else ""
    # unten rechts
    chars += (
        puzzle[below][right]
        if below < len(puzzle) and right < len(puzzle[y])
        else ""
    )
    # oben
    chars += puzzle[above][left:right] if above >= 0 else ""
    # unten
    chars += puzzle[below][left:right] if below < len(puzzle) else ""

    for s in sym:
        if s in chars:
            has_it.append(True)
        else:
            has_it.append(False)

    return any(has_it)


for y, anr in enumerate(all_numeric_ranges):
    for part in anr:
        if has_symbols(
            puzzle=puzzle_input,
            sym=part_number_chars,
            y=y,
            x1=part[0],
            x2=part[1],
        ):
            total.append(int(puzzle_input[y][part[0] : part[1] + 1]))


print_solution(solution=sum(total), y=year, d=day, part=1)
