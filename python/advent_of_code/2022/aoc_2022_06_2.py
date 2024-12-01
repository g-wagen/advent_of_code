from advent_of_code.helper import get_puzzle_input

puzzle_input = get_puzzle_input(y=2022, d=6)


def find_unique(data):
    for c, char in enumerate(data):
        if len(set(data[c : c + 14])) == 14:
            return c + 14


for line in puzzle_input:
    print(find_unique(line))
