from helper import get_puzzle_input, print_solution
import numpy as np

puzzle_input = get_puzzle_input(y=2022, d=9)
with open('aoc_2022_09_inputsample.txt', 'r') as f:
    puzzle_input = f.read().splitlines()

mapping = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}

head = [0, 0]
tail = [0, 0]
tail_positions: set = {(0, 0)}


def together(h, t):
    return abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1


def distance_x(hd, tl):
    return abs(hd[0] - tl[0])


def distance_y(hd, tl):
    return abs(hd[1] - tl[1])


def distance(head, tail):
    return tuple([distance_x(head, tail), distance_y(head, tail)])


def move_head():
    head[0] += mapping[direction][0]
    head[1] += mapping[direction][1]
    return head


head_positions = list()

for i in puzzle_input:
    direction = str(i.split(' ')[0])
    amount = int(i.split(' ')[1])

    # move head
    for j in range(amount):
        move_head()
        jo = tuple([head[0], head[1]])
        head_positions.append(jo)

special = []

for h, hpos in enumerate(head_positions):
    try:
        next_hpos = head_positions[h + 1]
    except IndexError:
        next_hpos = hpos

    if (distance(hpos, tail) or distance(next_hpos, tail)) <= (1, 1):
        tail_positions.add(tuple(tail))

    # up down left right
    if (distance(hpos, tail) == (1, 0) and distance(next_hpos, tail) == (2, 0)) or (
            distance(hpos, tail) == (0, 1) and distance(next_hpos, tail) == (0, 2)):
        tail = hpos
        tail_positions.add(tuple(hpos))

    if distance(hpos, tail) == distance(next_hpos, tail):
        tail_positions.add(tuple(tail))

    if distance(hpos, tail) == (1, 1) and distance(next_hpos, tail) > (1, 1):
        tail = head_positions.pop()
        tail_positions.add(tuple(tail))



field = np.full([8, 8], '.')

for p in tail_positions:
    field[p] = '#'

field[0, 0] = 's'

print(np.rot90(field))
