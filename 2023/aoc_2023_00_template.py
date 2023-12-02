from helper import choose_puzzle_input, print_solution

year = 123456
day = 1234567890

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


for line in puzzle_input:
    ...

print_solution(solution=0, y=year, d=day, part=1)


print_solution(solution=0, y=year, d=day, part=2)
