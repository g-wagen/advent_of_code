from aoc.helper import get_puzzle_input

calories = 0
elves = {}
elve_count = 0

puzzle_input = get_puzzle_input(y=2022, d=1)

for item in puzzle_input:
    try:
        item = int(item)
    except:
        item = None

    if item:
        calories += item
    else:
        elve_count += 1
        elves[elve_count] = calories
        calories = 0

max_calories = 0

for k, v in elves.items():
    if v > max_calories:
        max_calories = v

print(max_calories)
