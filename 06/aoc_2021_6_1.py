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

    for i, item in enumerate(data):
        if data[i] == 6 and prev[i] == 0:
            data = np.append(data, 8)

print(f'Lanternfish population after 80 days: {len(data)}')

