from advent_of_code.helper import print_solution, read_puzzle_input

year = 2025
day = 2

puzzle_input = read_puzzle_input(input_path="aoc_2025_02_input.txt")

ranges = []
for numbers in puzzle_input[0].split(","):
    start, end = numbers.split("-")
    ranges.append((int(start), int(end)))


def d2p1() -> int:
    solution = 0

    for numbers in ranges:
        for i in range(numbers[0], numbers[1] + 1):
            digits = str(i)
            if len(digits) % 2 == 0:
                num_digits = len(digits)
                half = int(num_digits / 2)

                part1, part2 = digits[:half], digits[half:]

                solution += int(f"{part1}{part2}") if part1 == part2 else 0

    return solution


def all_the_same(digits: list[str]) -> bool:
    return len(list(set([c for c in digits]))) == 1


def chunk_string(string: str, chunk: int) -> list[str]:
    return [string[i : i + chunk] for i in range(0, len(string), chunk)]


def d2p2() -> int:
    solution = 0

    for start, end in ranges:
        for num in [x for x in range(start, end + 1)]:
            number = str(num)

            for size in range(1, len(number)):
                chunks = chunk_string(number, size)
                if all_the_same(chunks):
                    solution += int(number)
                    break

    return solution


print_solution(solution=d2p1, y=year, d=day, part=1)

print_solution(solution=d2p2, y=year, d=day, part=2)
