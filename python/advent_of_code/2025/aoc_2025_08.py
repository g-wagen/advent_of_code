from collections import defaultdict

from math import sqrt

from advent_of_code.helper import print_solution, read_puzzle_input

year = 2025
day = 8

puzzle_input = read_puzzle_input(input_path="aoc_2025_08_input_sample.txt")
# puzzle_input = read_puzzle_input(input_path="aoc_2025_08_input.txt")


for i, line in enumerate(puzzle_input):
    puzzle_input[i] = [int(num) for num in line.split(",")]


def calculate_3d_distance(point1, point2) -> float:
    xdiff = abs(point2[0] - point1[0])
    ydiff = abs(point2[1] - point1[1])
    zdiff = abs(point2[2] - point1[2])

    return sqrt(xdiff**2 + ydiff**2 + zdiff**2)


def d8p1() -> int:
    solution = 1
    distances = {}
    points = {}


    for c, coord in enumerate(puzzle_input):
        points[tuple(coord)] = c

    for i, coord1 in enumerate(puzzle_input):
        for j, coord2 in enumerate(puzzle_input):
            if coord1 == coord2:
                continue
            point1, point2 = points[tuple(coord1)], points[tuple(coord2)]
            if (point2, point1) not in distances:
                distances[point1, point2] = calculate_3d_distance(coord1, coord2)

    distances = dict(sorted(distances.items(), key=lambda item: item[1]))

    connection_limit = 1000
    counter = 0

    circuits = []
    circuits.append(list(distances.keys())[0])

    for pair in distances.keys():
        pair = list(pair)
        if counter > connection_limit:
            break
        a, b = pair[0], pair[1]

        merged = False

        for g, group in enumerate(circuits):
            if a in group or b in group:
                circuits[g] = list(set(list(group) + pair))
                merged = True
                break

        if not merged:
            circuits.append(pair)

        counter += 1

    for c in circuits[:3]:
        solution *= len(c)

    return solution


def d8p2() -> int:
    solution = 0
    return solution


print_solution(solution=d8p1(), y=year, d=day, part=1)

print_solution(solution=d8p2(), y=year, d=day, part=2)
