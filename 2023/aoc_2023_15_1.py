from helper import choose_puzzle_input, print_solution

year = 2023
day = 15

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)

values = []

for i, wtf in enumerate(puzzle_input[0].split(",")):
    current = 0
    for w in wtf:
        current += ord(w)
        current *= 17
        current = current % 256
    values.append(current)


print_solution(solution=sum(values), y=year, d=day, part=1)
