from helper import choose_puzzle_input, print_solution

year = 2023
day = 14

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


def move_rock_up(ground: list, rocky: int, rockx: int):
    newground = [row.copy() for row in ground]
    newground[rocky][rockx] = "."
    newground[rocky - 1][rockx] = "O"
    return newground


def rock_coordinates(ground: list) -> list[tuple[int, int]]:
    for y in range(len(ground)):
        for x in range(len(ground[0])):
            if ground[y][x] == "O":
                yield y, x


floor_with_rocks = [[char for char in line] for line in puzzle_input]


while True:
    stop_moving = []

    for coord in rock_coordinates(ground=floor_with_rocks):
        up = coord[0] - 1
        if up >= 0 and floor_with_rocks[up][coord[1]] == ".":
            stop_moving.append(False)
            floor_with_rocks = move_rock_up(
                ground=floor_with_rocks,
                rocky=coord[0],
                rockx=coord[1],
            )
        else:
            stop_moving.append(True)

    if all(stop_moving):
        break

def calculate_load(ground: list) -> int:
    load = 0
    for y in range(len(ground)):
        for x in range(len(ground[0])):
            if ground[y][x] == "O":
                load += abs(y - len(ground))
    return load


load = calculate_load(ground=floor_with_rocks)

print_solution(solution=load, y=year, d=day, part=1)
