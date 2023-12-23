from aoc.helper import choose_puzzle_input, print_solution

year = 2023
day = 5

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)
seeds = [int(x) for x in puzzle_input[0].split(" ")[1:]]

sections = {}
last_key = ""

for line in puzzle_input[1:]:
    numbers = [x for x in line.split(" ")]
    if len(numbers) == 1:
        continue
    elif len(numbers) == 2:
        sections[numbers[0]] = []
        last_key = numbers[0]
    elif len(numbers) == 3:
        mapping = [int(x) for x in line.split(" ")]
        sections[last_key].append(mapping)


def calculate_location(seed_: int) -> int:
    prev_number: int = -1
    result = [seed_]

    if prev_number == -1:
        prev_number = seed_
    else:
        pass

    for sec, mapping in sections.items():
        for values in mapping:
            if values[1] <= prev_number <= values[1] + (values[2] - 1):
                prev_number = values[0] + prev_number - values[1]
                break
            else:
                prev_number = prev_number

        result.append(prev_number)

    return result[-1]


locations = []


for seed in seeds:
    locations.append(calculate_location(seed_=seed))

print_solution(solution=min(locations), y=year, d=day, part=1)
