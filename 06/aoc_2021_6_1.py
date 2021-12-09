import numpy
import helper
import numpy as np

data = ['3,4,3,1,2']
data = helper.get_puzzle_input(d=6, y=2021)
data = np.array([int(x) for x in data[0].split(',')])

prev = []

days = 80

for d in range(1, days + 1):
    prev = data.copy()
    data -= 1

    data = np.where(data == -1, 6, data)

    prev_has_zero = prev == 0
    data_has_six = data == 6

    compare = np.array([prev_has_zero, data_has_six]).T
    simple = np.all(compare, axis=1)
    add_multiplier = len(simple[simple == True])

    data = np.append(data, [8]*add_multiplier)

print(f'Lanternfish population after {days} days: {len(data)}')

