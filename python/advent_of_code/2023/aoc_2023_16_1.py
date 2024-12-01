from advent_of_code.helper import choose_puzzle_input, print_solution
import numpy as np
import sys

sys.setrecursionlimit(10**4)

year = 2023
day = 16

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


slash = "⟋"
backslash = "⟍"
minus = "-"
bar = "|"
dot = "."

tiles = [
    slash,
    backslash,
    minus,
    bar,
    dot,
]

data = np.array([[char for char in line] for line in puzzle_input])
data = np.where(data == "/", slash, data)
data = np.where(data == "\\", backslash, data)

visited = np.zeros(shape=data.shape, dtype=int)
start = (0, 0)


def move(terrain: np.array, y: int, x: int, heading: str, left: bool = True):
    if 0 > y or y > terrain.shape[0] - 1 or 0 > x or x > terrain.shape[1] - 1:
        return

    visited[y, x] = 1

    mapping = {
        "east": [y, x + 1],
        "south": [y + 1, x],
        "west": [y, x - 1],
        "north": [y - 1, x],
    }

    direction_change_mapping = {
        # \
        backslash: {
            "east": ["south"],
            "south": ["east"],
            "north": ["west"],
            "west": ["north"],
        },
        # /
        slash: {
            "east": ["north"],
            "south": ["west"],
            "north": ["east"],
            "west": ["south"],
        },
        # -
        minus: {
            "east": ["east"],
            "west": ["west"],
            "north": ["east", "west"],
            "south": ["east", "west"],
        },
        # |
        bar: {
            "east": ["north", "south"],
            "west": ["north", "south"],
            "north": ["north"],
            "south": ["south"],
        },
        # .
        dot: {
            "east": ["east"],
            "west": ["west"],
            "north": ["north"],
            "south": ["south"],
        },
    }
    new_heading = direction_change_mapping[terrain[y, x]][heading]
    new_heading = new_heading[0] if left else new_heading[1]

    new_y = mapping[new_heading][0]
    new_x = mapping[new_heading][1]

    if (
        0 > new_y
        or new_y > terrain.shape[0] - 1
        or 0 > new_x
        or new_x > terrain.shape[1] - 1
    ):
        return new_y, new_x, new_heading
    else:
        return -1, -1, ""


print(data)

towards = "east"
new_y = 0
new_x = 0
alternative_paths = set()

# for i in range(1000):
#     move_data = move(terrain=data, y=new_y, x=new_x, heading=towards)
#     if len(move_data) == 3:
#         new_y, new_x, towards = move_data[0], move_data[1], move_data[2]
#     else:
#         alternative_paths.add((move_data[0], move_data[1], move_data[2]))
#         alternative_paths.add((move_data[3], move_data[4], move_data[5]))


def recursive_move(
    terrain: np.array, y: int, x: int, heading: str, step: int, max_steps: int
):
    if step == max_steps:
        return

    move_data = move(terrain=terrain, y=y, x=x, heading=heading)
    if len(move_data) == 3:
        new_y, new_x, towards = move_data[0], move_data[1], move_data[2]
        recursive_move(
            terrain=terrain,
            y=new_y,
            x=new_x,
            heading=towards,
            step=step + 1,
            max_steps=max_steps - 1,
        )
        # visited[new_y, new_x] = 1
    else:
        recursive_move(
            terrain=terrain,
            y=move_data[0],
            x=move_data[1],
            heading=move_data[2],
            step=step + 1,
            max_steps=max_steps - 1,
        )
        recursive_move(
            terrain=terrain,
            y=move_data[3],
            x=move_data[4],
            heading=move_data[5],
            step=step + 1,
            max_steps=max_steps - 1,
        )

recursive_move(terrain=data, y=0, x=0, heading="east", step=0, max_steps=1000)
# print(alternative_paths)
print(visited)
print_solution(solution=0, y=year, d=day, part=1)
