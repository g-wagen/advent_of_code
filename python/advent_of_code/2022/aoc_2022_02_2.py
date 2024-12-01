from advent_of_code.helper import get_puzzle_input

puzzle_input = get_puzzle_input(y=2022, d=2)


def play(x):
    possibilities = {
        "A X": [False, 3],
        "A Y": [None, 4],
        "A Z": [True, 8],
        "B X": [False, 1],
        "B Y": [None, 5],
        "B Z": [True, 9],
        "C X": [False, 2],
        "C Y": [None, 6],
        "C Z": [True, 7],
    }

    output = 0

    for k, v in possibilities.items():
        if k == x:
            output = v[1]

    return x, output


points = 0

for item in puzzle_input:
    points += play(item)[1]

print(points)
