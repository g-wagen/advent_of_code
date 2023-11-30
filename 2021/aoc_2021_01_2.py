import helper

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

data = helper.get_puzzle_input(d=1, y=2021)

data = [int(x) for x in data]

increase = 0

for i, d in enumerate(data):
    section = data[i : i + 3]
    section_sum = sum(section)

    next_section = data[i + 1 : i + 4]
    next_section_sum = sum(next_section)

    if len(section) == 3 and len(next_section) == 3 and section_sum < next_section_sum:
        increase += 1

print(f"increased {increase} times")
