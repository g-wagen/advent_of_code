from advent_of_code.helper import print_solution, read_puzzle_input

year = 2025
day = 5

puzzle_input = read_puzzle_input(input_path="aoc_2025_05_input.txt")


# puzzle_input = read_puzzle_input(input_path="aoc_2025_05_input_sample.txt")


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


def d5p2() -> int:
    ingredient_ids = set()
    fresh_ingredient_ranges: dict[range, int] = {}
    fresh_ingredients = set()

    for l, line in enumerate(puzzle_input):
        if "-" in line:
            start, end = line.split("-")
            fresh_range = range(int(start), int(end) + 1, 1)
            fresh_ingredient_ranges[fresh_range] = len(fresh_range)

    # print(fresh_ingredient_ranges)

    return 123


print_solution(solution=d5p1(), y=year, d=day, part=1)

print_solution(solution=d5p2(), y=year, d=day, part=2)
