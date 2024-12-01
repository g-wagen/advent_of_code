from advent_of_code.helper import choose_puzzle_input, print_solution

year = 2023
day = 21

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


the_map = [
    [9 if tile == "S" else 1 if tile == "." else 0 for tile in line]
    for line in puzzle_input
]


def walk_north(terrain: list[list[int]], y: int, x: int):
    if y - 1 >= 0 and terrain[y - 1][x] != 0:
        return y - 1, x
    return None


def walk_east(terrain: list[list[int]], y: int, x: int):
    if x + 1 < len(terrain[y]) and terrain[y][x + 1] != 0:
        return y, x + 1
    return None


def walk_south(terrain: list[list[int]], y: int, x: int):
    if y + 1 < len(terrain) and terrain[y + 1][x] != 0:
        return y + 1, x
    return None


def walk_west(terrain: list[list[int]], y: int, x: int):
    if x - 1 >= 0 and terrain[y][x - 1] != 0:
        return y, x - 1
    return None


def find_start(terrain: list[list[int]]) -> tuple[int, int]:
    for y in range(len(terrain) - 1):
        for x in range(len(terrain[0]) - 1):
            if terrain[y][x] == 9:
                return y, x


def find_positions(terrain: list[list[int]], y: int, x: int):
    north = walk_north(terrain=terrain, y=y, x=x)
    east = walk_east(terrain=terrain, y=y, x=x)
    south = walk_south(terrain=terrain, y=y, x=x)
    west = walk_west(terrain=terrain, y=y, x=x)

    return [direction for direction in [north, east, south, west] if direction]


start_position = find_start(terrain=the_map)
max_steps = 64
positions_collection = []

for i in range(max_steps):
    if not positions_collection:
        positions_collection.append(
            find_positions(
                terrain=the_map, y=start_position[0], x=start_position[1]
            )
        )
    else:
        new_positions = []
        for pos in positions_collection[-1]:
            new_positions.extend(
                find_positions(terrain=the_map, y=pos[0], x=pos[1])
            )
        positions_collection.append(list(set(new_positions)))

reached_plots = len(positions_collection[-1])

print_solution(solution=reached_plots, y=year, d=day, part=1)
