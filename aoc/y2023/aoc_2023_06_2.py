from aoc.helper import choose_puzzle_input, print_solution

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
    data[splitted[0]] = int("".join(splitted[1:]))


def race(hold_time: int, total_race_duration: int):
    time_difference = total_race_duration - hold_time
    return time_difference * hold_time


ways_to_win = []

p = 0
for t_ in range(data["Time"]):
    print(f"{t_}/{data['Time']}")
    dist = race(hold_time=t_, total_race_duration=data["Time"])
    if dist > data["Distance"]:
        p += 1
    ways_to_win.append(p)


print_solution(solution=max(ways_to_win), y=year, d=day, part=2)
