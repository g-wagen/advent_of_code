from advent_of_code.helper import choose_puzzle_input, print_solution

year = 2023
day = 10

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)

start = None

possible_tiles = ["7", "L", ".", "S", "J", "F", "|", "-"]

visited_1 = []
visited_2 = []


def start_connections(maze: list[str], startpos: list[int]) -> list[list[int]]:
    up = startpos[0] - 1
    down = startpos[0] + 1
    left = startpos[1] - 1
    right = startpos[1] + 1
    x, y = startpos[1], startpos[0]

    tile_up, tile_down, tile_left, tile_right = None, None, None, None

    if up >= 0 and maze[up][x] in ["7", "F", "|"]:
        tile_up = {"coord": [up, x], "tile": maze[up][x]}
    if down < len(maze) and maze[down][x] in ["L", "J", "|"]:
        tile_down = {"coord": [down, x], "tile": maze[down][x]}
    if left >= 0 and maze[y][left] in ["L", "F", "-"]:
        tile_left = {"coord": [y, left], "tile": maze[y][left]}
    if right < len(maze[0]) and maze[y][right] in ["7", "J", "-"]:
        tile_right = {"coord": [y, right], "tile": maze[y][right]}

    next_coordinates = [
        [tile["coord"][0], tile["coord"][1]]
        for tile in [tile_up, tile_down, tile_left, tile_right]
        if tile
    ]

    return next_coordinates


def next_connection(
    maze: list[str], startpos: list[int], prevpos: list[list[int]]
) -> list[int]:
    up = startpos[0] - 1
    down = startpos[0] + 1
    left = startpos[1] - 1
    right = startpos[1] + 1
    x, y = startpos[1], startpos[0]

    tile_up, tile_down, tile_left, tile_right = None, None, None, None

    if (
        up >= 0
        and maze[up][x] in ["7", "F", "|"]
        and maze[y][x] in ["L", "J", "|"]
    ):
        tile_up = [up, x]
    if (
        down < len(maze)
        and maze[down][x] in ["L", "J", "|"]
        and maze[y][x] in ["7", "F", "|"]
    ):
        tile_down = [down, x]
    if (
        left >= 0
        and maze[y][left] in ["L", "F", "-"]
        and maze[y][x] in ["7", "J", "-"]
    ):
        tile_left = [y, left]
    if (
        right < len(maze[0])
        and maze[y][right] in ["7", "J", "-"]
        and maze[y][x] in ["L", "F", "-"]
    ):
        tile_right = [y, right]

    next_coordinates = [
        [tile[0], tile[1]]
        for tile in [tile_up, tile_down, tile_left, tile_right]
        if tile and [tile[0], tile[1]] not in prevpos
    ][0]

    return next_coordinates


for y, line in enumerate(puzzle_input):
    start_index = line.find("S")
    if start_index > -1:
        start = [y, start_index]
        break

start_conns = start_connections(maze=puzzle_input, startpos=start)
visited_1.append(start_conns[0])
visited_2.append(start_conns[1])

while visited_1[-1] != visited_2[-1]:
    visited_1.append(
        next_connection(
            maze=puzzle_input, startpos=visited_1[-1], prevpos=visited_1
        )
    )
    visited_2.append(
        next_connection(
            maze=puzzle_input, startpos=visited_2[-1], prevpos=visited_2
        )
    )


solution = len(visited_1) if len(visited_1) == len(visited_2) else None
print_solution(solution=solution, y=year, d=day, part=1)
