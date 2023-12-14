from string import ascii_lowercase, ascii_uppercase
from helper import get_puzzle_input, make_chunks

puzzle_input = get_puzzle_input(y=2022, d=3)

prios_lower = {x: i + 1 for i, x in enumerate(ascii_lowercase)}
prios_upper = {
    y: i + 1 + len(prios_lower) for i, y in enumerate(ascii_uppercase)
}


def find_common_item(rucksacks):
    sets = [set(r) for r in rucksacks]
    common = set.intersection(*sets)
    return common.pop()


def get_prio(item):
    if item in prios_lower:
        return prios_lower[item]
    elif item in prios_upper:
        return prios_upper[item]


groups = make_chunks(3, puzzle_input)

sum_of_prios = 0
for grp in groups:
    common_group_item = find_common_item(grp)
    sum_of_prios += get_prio(common_group_item)


print(sum_of_prios)
