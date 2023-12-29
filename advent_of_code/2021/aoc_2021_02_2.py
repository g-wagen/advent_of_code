from advent_of_code import helper

data = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]

data = helper.get_puzzle_input(d=2, y=2021)

horiz = 0
depth = 0
aim = 0

for instr in data:
    direction = instr.split()[0]
    amount = int(instr.split()[1])

    if direction == "forward":
        horiz += amount
        if aim != 0:
            depth += aim * amount
    if direction == "up":
        aim -= amount
    if direction == "down":
        aim += amount

print(f"Horizontal * Depth (AND AIM): {horiz * depth}")
