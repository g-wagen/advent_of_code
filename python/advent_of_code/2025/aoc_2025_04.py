from advent_of_code.helper import print_solution, read_puzzle_input

year = 2025
day = 4

puzzle_input = read_puzzle_input(input_path="aoc_2025_04_input.txt")


def pad_grid(grid: list[str]) -> list[list[str]]:
    extra_row = ["." for _ in range(len(grid[0]) + 2)]
    padded = []
    padded.append(extra_row)
    for row in grid:
        padded.append([".", *[x for x in row], "."])
    padded.append(extra_row)
    return padded


def get_neighbors(grid, row, x, y) -> list[str]:
    return [row[x - 1], row[x + 1], grid[y - 1][x], grid[y + 1][x], grid[y - 1][x - 1], grid[y - 1][x + 1],
            grid[y + 1][x - 1], grid[y + 1][x + 1]]


def d4p1() -> int:
    solution = 0

    grid = pad_grid(puzzle_input)

    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if item == "@":
                items = get_neighbors(grid, row, x, y)
                rolls_nearby = items.count("@")

                if rolls_nearby < 4:
                    solution += 1

    return solution


def d4p2() -> int:
    solution = 0

    grid = pad_grid(puzzle_input)

    while True:
        access_counts = []
        for y, row in enumerate(grid):
            for x, item in enumerate(row):
                if item == "@":
                    items = get_neighbors(grid, row, x, y)
                    rolls_nearby = items.count("@")

                    if rolls_nearby < 4:
                        solution += 1
                        # remove paper roll
                        grid[y][x] = "."

                    access_counts.append(rolls_nearby)

        if min(access_counts) > 3:
            break

    return solution


print_solution(solution=d4p1(), y=year, d=day, part=1)

print_solution(solution=d4p2(), y=year, d=day, part=2)
