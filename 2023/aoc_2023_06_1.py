from helper import choose_puzzle_input, print_solution

year = 2023
day = 6

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)

data = {}

for line in puzzle_input:
    splitted = line.replace(":", "").split(" ")
    data[splitted[0]] = [int(x) for x in splitted[1:] if x]


def race(hold_time: int, total_race_duration: int):
    time_difference = total_race_duration - hold_time
    return time_difference * hold_time


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


print_solution(solution=ways_to_win, y=year, d=day, part=1)
