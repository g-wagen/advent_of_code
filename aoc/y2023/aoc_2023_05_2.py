from typing import Iterable
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
        destination_range = range(mapping[0], mapping[0] + mapping[2])
        source_range = range(mapping[1], mapping[1] + mapping[2])
        sections[last_key].append([destination_range, source_range])


def calculate_location(seed_: int) -> int:
    prev_number: int = -1
    result = [seed_]

    if prev_number == -1:
        prev_number = seed_
    else:
        pass

    for sec, mapping in sections.items():
        for values in mapping:
            dest_range = values[0]
            src_range = values[1]
            if prev_number in src_range:
                prev_number = dest_range.start + src_range.index(prev_number)
                break
            else:
                prev_number = prev_number

        result.append(prev_number)

    return result[-1]


def get_min_location(the_batch):
    return min(map(calculate_location, the_batch))


def chunk(iterable: Iterable, size: int) -> Iterable:
    for i in range(0, len(iterable), size):
        yield iterable[i : i + size]


seed_chunks = chunk(seeds, 2)
batchsize = 1000000
locations = []


for r, rng in enumerate(seed_chunks):
    whole_range = range(rng[0], rng[0] + rng[1])
    num_items = len(whole_range)
    for j, batch in enumerate(chunk(whole_range, batchsize)):
        current = (j + 1) * batchsize
        print(
            f"Seed batch {r+1} - {current}/{num_items} - {(current / num_items) * 100} %"
        )
        locations.append(get_min_location(batch))


print_solution(solution=min(locations), y=year, d=day, part=2)
