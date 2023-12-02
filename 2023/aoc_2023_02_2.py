from helper import choose_puzzle_input, print_solution

year = 2023
day = 2

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


powers = []
for line in puzzle_input:
    minimums = {"red": 0, "green": 0, "blue": 0}
    game, moves = line.split(":")
    the_id = int(game.split()[-1].strip())
    cube_sets = moves.split(";")
    for cubes in cube_sets:
        cube = cubes.split(",")
        for c in cube:
            amount = int(c.split()[0].strip())
            color = c.split()[-1].strip()

            if minimums[color] < amount:
                minimums[color] = amount

    pwr = 0
    for i in minimums.values():
        if pwr == 0:
            pwr += i
        else:
            pwr *= i

    powers.append(pwr)

print_solution(solution=sum(powers), y=year, d=day, part=2)
