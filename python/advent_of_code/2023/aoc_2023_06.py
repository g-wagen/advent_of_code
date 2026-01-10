from advent_of_code.helper import read_puzzle_input, print_solution

year = 2023
day = 6

puzzle_input = read_puzzle_input(input_path=f"aoc_{year}_{day:02d}_input.txt")

def race(hold_time: int, total_race_duration: int):
    time_difference = total_race_duration - hold_time
    return time_difference * hold_time

def y2023d6p1():
    data = {}

    for line in puzzle_input:
        splitted = line.replace(":", "").split(" ")
        data[splitted[0]] = [int(x) for x in splitted[1:] if x]

    ways_to_win = 0

    for t, d in zip(data["Time"], data["Distance"]):
        p = 0
        for t_ in range(t):
            dist = race(hold_time=t_, total_race_duration=t)
            if dist > d:
                p += 1
        if ways_to_win == 0:
            ways_to_win = p
        else:
            ways_to_win *= p

    return ways_to_win

def y2023d6p2():
    data = {}

    for line in puzzle_input:
        splitted = line.replace(":", "").split(" ")
        data[splitted[0]] = int("".join(splitted[1:]))

    ways_to_win = []

    p = 0
    for t_ in range(data["Time"]):
        dist = race(hold_time=t_, total_race_duration=data["Time"])
        if dist > data["Distance"]:
            p += 1
        ways_to_win.append(p)

    return max(ways_to_win)

print_solution(solution=y2023d6p1, y=year, d=day, part=1)

print_solution(solution=y2023d6p2, y=year, d=day, part=2)