from advent_of_code.helper import read_puzzle_input, print_solution

year = 2023
day = 2

puzzle_input = read_puzzle_input(input_path=f"aoc_{year}_{day:02d}_input.txt")

def y2023d2p1():
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
    return sum(games)

def y2023d2p2():
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

    return sum(powers)


print_solution(solution=y2023d2p1, y=year, d=day, part=1)

print_solution(solution=y2023d2p2, y=year, d=day, part=2)
