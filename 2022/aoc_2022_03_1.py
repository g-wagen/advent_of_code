from helper import get_puzzle_input
from string import ascii_lowercase, ascii_uppercase

puzzle_input = get_puzzle_input(y=2022, d=3)

prios_lower = {x: i + 1 for i, x in enumerate(ascii_lowercase)}
prios_upper = {
    y: i + 1 + len(prios_lower) for i, y in enumerate(ascii_uppercase)
}


def first_comp(rucksack):
    return rucksack[: len(rucksack) // 2]


def second_comp(rucksack):
    return rucksack[len(rucksack) // 2 :]


def get_extra(rucksack):
    first = set(first_comp(rucksack))
    second = set(second_comp(rucksack))
    extra = first.intersection(second)
    return extra.pop()


def get_prio(item):
    if item in prios_lower:
        return prios_lower[item]
    elif item in prios_upper:
        return prios_upper[item]


sum_of_prios = 0

for rucksack in puzzle_input:
    extra = get_extra(rucksack)
    sum_of_prios += get_prio(extra)

print(sum_of_prios)
