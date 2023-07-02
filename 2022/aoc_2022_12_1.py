import concurrent.futures
import multiprocessing
from copy import copy, deepcopy
from random import choice


from helper import print_solution, choose_puzzle_input, get_puzzle_input
import numpy as np
from string import ascii_lowercase


puzzle_input = choose_puzzle_input(y=2022, d=12, sample_input_path="aoc_2022_12_inputsample.txt")

lowercase = {'S': 0}
lowercase.update({l: i+1 for l, i in zip(ascii_lowercase, range(len(ascii_lowercase)))})
lowercase.update({'E': len(ascii_lowercase)+1})
axis_y = len(puzzle_input)
axis_x = len(puzzle_input[0])
data = [lowercase[x] for x in ''.join(puzzle_input)]
new_data = list()

data = np.array(data).reshape((axis_y, axis_x))
print(data)

min_value = np.min(data)
max_value = np.max(data)

start_coords = np.array(np.where(data == np.min(data))).flatten()
end_coords = np.array(np.where(data == np.max(data))).flatten()

print(start_coords, end_coords)

def get_value(grid, coords: list):
    return grid[coords[0], coords[1]]

def at_target(grid, coords: list, value: int) -> bool:
    return get_value(grid=grid, coords=coords) == value


# def next_ok(current_coords: list, next_coords: list) -> bool:
#     current_evaluation = data[current_coords[0], current_coords[1]]
#     next_evaluation = data[next_coords[0], next_coords[1]]
#     return next_evaluation == current_evaluation + 1 or next_evaluation == current_evaluation

def next_ok(grid, current_value: int, next_coords: list) -> bool:
    next_evaluation = get_value(grid=grid, coords=next_coords)
    return next_evaluation == current_value + 1 or next_evaluation == current_value


def next_steps(grid, current_coords: list) -> list[list]:
    if current_coords[0] >= data.shape[0] or current_coords[1] >= data.shape[1] or current_coords[0] < 0 or current_coords[1] < 0:
        raise IndexError

    above_coords = [current_coords[0]-1, current_coords[1]]
    below_coords = [current_coords[0]+1, current_coords[1]]
    left_coords = [current_coords[0], current_coords[1]-1]
    right_coords = [current_coords[0], current_coords[1]+1]

    valid_next_steps = list()

    for coords in [above_coords, below_coords, left_coords, right_coords]:
        # coordinates outside the 2d array are not valid
        if coords[0] < 0 or coords[0] >= grid.shape[0]:
            coords[0] = None
        if coords[1] < 0 or coords[1] >= grid.shape[1]:
            coords[1] = None

        # only append valid coordinates
        if None not in coords:
            valid_next_steps.append(coords)

    return valid_next_steps


def make_unattractive(grid, current_coords: list):
    grid[current_coords[0], current_coords[1]] = -1


class MyCounter:
    counter = 0
    results = set()


my_counter = MyCounter()


"""
begin from start_coords

assume current coordinates as new start coordinates
check current position for end condition
true: 
 - return
false: 
 - make current position unattractive
 - search for new coordinates to go to
 - test each new coordinate for plausability
 - branch off to new coordinates and repeat

"""

def search(grid, start):
    current_value = get_value(grid=grid, coords=start)

    if at_target(grid=grid, coords=start, value=max_value):
        # print("hit")
        my_counter.results.add(my_counter.counter)
        return my_counter.counter

    make_unattractive(grid=grid, current_coords=start)

    possibilities = next_steps(grid=grid, current_coords=start)
    really_next = []
    for poss in possibilities:
        if next_ok(grid=grid, current_value=current_value, next_coords=poss):
            really_next.append(poss)

    if len(really_next) > 0:
        the_next = choice(really_next)
        my_counter.counter += 1
        search(grid=grid, start=the_next)

    return False

# This brute force approach does not work on a big dataset

iterations = range(1000)

def do_stuff(x):
    my_counter.counter = 0
    workdata = deepcopy(data)
    if search(grid=workdata, start=start_coords):
        print(my_counter.counter)
        return my_counter.counter

# for i in range(1000):
#     my_counter.counter = 0
#     workdata = deepcopy(data)
#     # print(my_counter.counter)
#     # print(f"Brute force iteration {i}")
#     if search(grid=workdata, start=start_coords):
#         print(i, my_counter.counter)

bleh = list(map(do_stuff, iterations))

print(min(my_counter.results))
