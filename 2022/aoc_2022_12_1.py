from helper import choose_puzzle_input, print_solution
from string import ascii_lowercase

year = 2022
day = 12

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)
move_order = f"S{ascii_lowercase}E"

moves_map = {c: d for c, d in zip(move_order, range(len(move_order)))}
print(moves_map)


data = []
start = None
end = None

for l, line in enumerate(puzzle_input):
    print(line)
    find_start = line.find("S")
    find_end = line.find("E")
    if find_start > -1:
        start = [l, find_start]
    elif find_end > -1:
        end = [l, find_end]
    else:
        pass

print(start)
print(end)

print_solution(solution=0, y=year, d=day, part=1)
