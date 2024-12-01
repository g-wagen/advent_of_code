from advent_of_code.helper import choose_puzzle_input, print_solution

year = 2023
day = 4

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)

total_points = 0

for line in puzzle_input:
    winning, have = line.split("|")
    winning = winning.split(":")[1]
    winning = [int(w) for w in winning.split()]
    have = [int(h) for h in have.split()]
    points = 0
    for h in have:
        if h in winning:
            if points == 0:
                points += 1
            else:
                points *= 2
    total_points += points


print_solution(solution=total_points, y=year, d=day, part=1)
