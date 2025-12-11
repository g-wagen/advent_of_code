from advent_of_code.helper import print_solution, read_puzzle_input

year = 2025
day = 3

# puzzle_input = read_puzzle_input(input_path="aoc_2025_03_input.txt")
puzzle_input = read_puzzle_input(input_path="aoc_2025_03_input_sample.txt")


def d3p1() -> int:
    solution = 0
    for bank in puzzle_input:
        joltages = set()

        for b, first_battery in enumerate(bank):
            for bb, second_battery in enumerate(bank[b + 1 :]):
                joltages.add(int(f"{first_battery}{second_battery}"))

        solution += max(joltages)

    return solution


def d3p2() -> int:
    solution = 0
    for bank in puzzle_input:
        numbers = [int(x) for x in bank]
        joltage = []

        len_nums = len(numbers)
        prev_item = None
        next_item = None

        numbers_needed = 12
        discarded = 0
        max_discard = len(bank) - numbers_needed

        for n, num in enumerate(numbers):
            if n > 0:
                prev_item = numbers[n - 1]
            if n < (len_nums - 1):
                next_item = numbers[n + 1]

            if n == len_nums:
                next_item = None

            if num >= next_item:
                joltage.append(num)

        print("".join([str(x) for x in joltage]))

    return solution


print_solution(solution=d3p1(), y=year, d=day, part=1)

print_solution(solution=d3p2(), y=year, d=day, part=2)
