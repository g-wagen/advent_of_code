import numpy
import helper
import numpy as np


def get_distance(a, b):
    return abs(b - a)


data = ['16,1,2,0,4,2,7,1,2,14']
data = helper.get_puzzle_input(d=7, y=2021)
data = np.array([int(x) for x in data[0].split(',')])

consumed_fuel = []
position = 0
while position < len(data):
    fuel = 0
    for d in data:
        fuel += get_distance(d, position)
    consumed_fuel.append(fuel)
    position += 1

min_fuel = min(consumed_fuel)
best_position = consumed_fuel.index(min_fuel)

print(f'Horizontal position: {best_position}\n'
      f'Fuel consumption: {min_fuel}')
