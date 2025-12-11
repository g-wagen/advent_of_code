from advent_of_code.helper import print_solution, read_puzzle_input

year = 2025
day = 7

puzzle_input = read_puzzle_input(input_path="aoc_2025_07_input_sample.txt")
# puzzle_input = read_puzzle_input(input_path="aoc_2025_07_input.txt")

grid = [[str(x) for x in line] for line in puzzle_input]

def d7p1() -> int:
    solution = 0

    # initial beam
    grid[1][grid[0].index("S")] = "|"

    for r, row in enumerate(grid):
        for c, column in enumerate(row):
            if column == "^" and grid[r-1][c] == "|":
                # split the beam
                row[c-1] = "|"
                row[c+1] = "|"
                solution += 1

            if grid[r-1][c] == "|" and column != "^":
                row[c] = "|"

    for line in grid:
        print("".join(line))

    return solution


def d7p2() -> int:
    solution = 0
    # depth first search?
    return solution


print_solution(solution=d7p1(), y=year, d=day, part=1)

print_solution(solution=d7p2(), y=year, d=day, part=2)
