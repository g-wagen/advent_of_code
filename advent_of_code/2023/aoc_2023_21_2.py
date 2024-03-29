from advent_of_code.helper import choose_puzzle_input, print_solution

year = 2023
day = 21

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


the_map = [
    [9 if tile == "S" else 1 if tile == "." else 0 for tile in line]
    for line in puzzle_input
]


def walk_everywhere(terrain: list[list[int]], y: int, x: int):
    north = y - 1
    south = y + 1
    east = x + 1
    west = x - 1
    north_safe = north % len(terrain)
    east_safe = east % len(terrain[0])
    south_safe = south % len(terrain)
    west_safe = west % len(terrain[0])
    y_safe = y % len(terrain)
    x_safe = x % len(terrain[0])

    positions = []
    if terrain[north_safe][x_safe] != 0:
        positions.append((north, x))
    if terrain[y_safe][east_safe] != 0:
        positions.append((y, east))
    if terrain[south_safe][x_safe] != 0:
        positions.append((south, x))
    if terrain[y_safe][west_safe] != 0:
        positions.append((y, west))

    return positions


def find_start(terrain: list[list[int]]) -> tuple[int, int]:
    for y in range(len(terrain) - 1):
        for x in range(len(terrain[0]) - 1):
            if terrain[y][x] == 9:
                return y, x


def calculate_reached_garden_plots(terrain: list[list[int]], steps: int) -> int:
    start_position = find_start(terrain=terrain)

    positions_collection = [
        walk_everywhere(
            terrain=terrain,
            y=start_position[0],
            x=start_position[1],
        )
    ]

    for i in range(1, steps):
        new_positions = []
        for pos in positions_collection[-1]:
            new_positions.extend(
                walk_everywhere(terrain=terrain, y=pos[0], x=pos[1])
            )
        positions_collection.append(list(set(new_positions)))
        del positions_collection[0]

    reached_plots = len(positions_collection[-1])
    return reached_plots


# Who wants to wait forever?
print_solution(
    solution=calculate_reached_garden_plots(terrain=the_map, steps=26501365),
    y=year,
    d=day,
    part=2,
)
