import helper

data = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]

data = helper.get_puzzle_input(d=3, y=2021)

counter = [0] * len(data[0])
max_len = [len(data)] * len(counter)
gamma = ''

for d in data:
    for i, b in enumerate(d):
        counter[i] += int(b)

for i, c in enumerate(counter):
    gamma += '1' if c > max_len[i]/2 else '0'

gamma_dec = (int(gamma, 2))

epsilon = ''
for g in gamma:
    if int(g) == 0:
        epsilon += '1'
    elif int(g) == 1:
        epsilon += '0'

epsilon_dec = (int(epsilon, 2))

print(f'power consumption: {gamma_dec * epsilon_dec}')