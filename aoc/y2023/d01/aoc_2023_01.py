from aoc.helper import choose_puzzle_input, print_solution

puzzle_input = choose_puzzle_input(
    y=2023,
    d=1,
    # sample_input_path="aoc_2023_01_input_sample.txt",
)

total_1 = []
for line in puzzle_input:
    digits = ""

    for char in line:
        if char.isnumeric():
            digits += char
            break

    for char in line[::-1]:
        if char.isnumeric():
            digits += char
            break

    total_1.append(int(digits))

print_solution(solution=sum(total_1), y=2023, d=1, part=1)


puzzle_input = choose_puzzle_input(
    y=2023,
    d=1,
    # sample_input_path="aoc_2023_01_input_sample2.txt",
)

numberdigits = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


total_2 = []
for line in puzzle_input:
    out = ""
    for index in range(len(line)):
        for k, v in numberdigits.items():
            if line.startswith(k, index):
                out += str(v)
    total_2.append(int(f"{out[0]}{out[-1]}"))


print_solution(solution=sum(total_2), y=2023, d=1, part=2)
