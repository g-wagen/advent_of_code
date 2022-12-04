from helper import get_puzzle_input

puzzle_input = get_puzzle_input(y=2022, d=2)


def play(input_data: str):
    win_lose_matrix = [
        # r, p, s
        [-1, 1, 0],  # r
        [0, -1, 1],  # p
        [1, 0, -1]   # s
    ]

    matrix_mapping = {
        'A': 0,
        'B': 1,
        'C': 2,
        'X': 0,
        'Y': 1,
        'Z': 2
    }

    splititem = input_data.split(' ')

    my_shape = matrix_mapping[splititem[1]]
    my_shape_score = my_shape + 1
    opponent_shape = matrix_mapping[splititem[0]]

    outcome = win_lose_matrix[opponent_shape][my_shape]

    round_score = 0

    if outcome > 0:
        round_score += my_shape_score + 6
    elif outcome < 0:
        round_score += my_shape_score + 3
    else:
        round_score += my_shape_score

    return round_score


total_score = 0

for item in puzzle_input:
    total_score += play(item)

print(total_score)
