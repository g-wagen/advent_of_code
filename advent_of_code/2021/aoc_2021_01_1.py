from advent_of_code import helper

data = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]

data = [int(x) for x in helper.get_puzzle_input(d=1, y=2021)]

increase = 0

first = data[0]
for d in data[1:]:
    if d > first:
        increase += 1

    first = d

print(f"increased {increase} times")
