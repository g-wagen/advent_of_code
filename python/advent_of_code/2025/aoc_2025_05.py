from advent_of_code.helper import print_solution, read_puzzle_input

year = 2025
day = 5

puzzle_input = read_puzzle_input(input_path="aoc_2025_05_input.txt")


def d5p1() -> int:
    ingredient_ids = set()
    fresh_ingredient_ranges: list[range] = []
    fresh_ingredients = set()

    for l, line in enumerate(puzzle_input):
        if "-" in line:
            start, end = line.split("-")
            fresh_ingredient_ranges.append(range(int(start), int(end) + 1, 1))
        elif line != "" and "-" not in line:
            ingredient_ids.add(int(line))

    for ingredient in ingredient_ids:
        for r in fresh_ingredient_ranges:
            if ingredient in r:
                fresh_ingredients.add(ingredient)

    return len(fresh_ingredients)


def overlapping(range1, range2) -> bool:
    max_start = max(range1[0], range2[0])
    min_end = min(range1[1], range2[1])

    return max_start <= min_end + 1


def combine_range(range1, range2) -> list[int]:
    return [min(range1[0], range2[0]), max(range1[1], range2[1])]


def d5p2() -> int:
    solution = 0

    ingredient_ranges = []
    for line in puzzle_input:
        if "-" in line:
            start, end = line.split("-")
            ingredient_ranges.append([int(start), int(end)])

    ingredient_ranges = sorted(ingredient_ranges, key=lambda x: x[0])

    merged = True

    while merged:
        merged = False
        for i, r in enumerate(ingredient_ranges):
            try:
                if overlapping(r, ingredient_ranges[i + 1]):
                    merged = True
                    new_range = combine_range(r, ingredient_ranges[i + 1])
                    ingredient_ranges[i] = new_range
                    del ingredient_ranges[i + 1]
                    break
            except IndexError:
                pass

    for id in ingredient_ranges:
        solution += (id[1] + 1) - id[0]

    return solution


print_solution(solution=d5p1, y=year, d=day, part=1)

print_solution(solution=d5p2, y=year, d=day, part=2)
