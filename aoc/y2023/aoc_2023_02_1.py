from aoc.helper import choose_puzzle_input, print_solution

year = 2023
day = 2

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)

possible = {"red": 12, "green": 13, "blue": 14}

games = []
for line in puzzle_input:
    game_possible = []
    game, moves = line.split(":")
    the_id = int(game.split()[-1].strip())
    cube_sets = moves.split(";")
    for cubes in cube_sets:
        cube = cubes.split(",")
        for c in cube:
            amount = int(c.split()[0].strip())
            color = c.split()[-1].strip()
            if possible[color] >= amount:
                game_possible.append(True)
            else:
                game_possible.append(False)
    if all(game_possible):
        games.append(the_id)


print_solution(solution=sum(games), y=year, d=day, part=1)
