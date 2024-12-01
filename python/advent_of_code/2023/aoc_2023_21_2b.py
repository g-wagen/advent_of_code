from time import perf_counter

from advent_of_code.helper import choose_puzzle_input

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


class Storage:
    def __init__(self, terrain: list[list[int]]):
        self.terrain = terrain
        self.width = len(self.terrain[0])
        self.height = len(self.terrain)
        self.storage = {}
        for y in range(self.height):
            for x in range(self.width):
                self.storage[(y, x)] = []

    def read(self) -> list[tuple[int, int]]:
        output = []
        for v in self.storage.values():
            output.extend(v)
        return list(set(output))

    def write(self, values: list[tuple[int, int]]):
        for value in values:
            y_safe = value[0] % self.height
            x_safe = value[1] % self.width
            self.storage[(y_safe, x_safe)].append(value)

    def clear(self):
        self.storage = dict.fromkeys(self.storage.keys(), [])


def walk_everywhere(
    terrain: list[list[int]], y: int, x: int
) -> list[tuple[int, int]]:
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


def calculate_reached_garden_plots(steps: int, storage: Storage) -> int:
    start_position = find_start(terrain=storage.terrain)

    storage.write(
        walk_everywhere(
            terrain=storage.terrain,
            y=start_position[0],
            x=start_position[1],
        )
    )
    last_values = []

    for i in range(steps):
        last_values = storage.read()
        storage.clear()
        storage.write([
            result
            for v in last_values
            for result in walk_everywhere(
                terrain=storage.terrain, y=v[0], x=v[1]
            )
        ])

    reached_plots = len(last_values)
    return reached_plots


my_storage = Storage(terrain=the_map)
start = perf_counter()
print(calculate_reached_garden_plots(steps=500, storage=my_storage))
print(f"Execution time: {perf_counter()-start} seconds")
# print_solution(solution=reached_plots, y=year, d=day, part=2)
# print(f"Execution time: {end} seconds")
