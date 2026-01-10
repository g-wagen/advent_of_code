from advent_of_code.helper import read_puzzle_input, print_solution

year = 2023
day = 4

puzzle_input = read_puzzle_input(input_path=f"aoc_{year}_{day:02d}_input.txt")


def y2023d4p1():
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

    return total_points

def y2023d4p2():
    total_cards = {}

    for l, line in enumerate(puzzle_input):
        total_cards[l] = 1

    for l, line in enumerate(puzzle_input):
        winning, have = line.split("|")
        winning = winning.split(":")[1]
        winning = [int(w) for w in winning.split()]
        have = [int(h) for h in have.split()]
        win_cards = 0
        for h in have:
            win = 0
            if h in winning:
                win_cards += 1

        if win_cards > 0:
            for w in range(win_cards):
                total_cards[l + w + 1] += 1 * total_cards[l]


    return sum(total_cards.values())


print_solution(solution=y2023d4p1, y=year, d=day, part=1)

print_solution(solution=y2023d4p2, y=year, d=day, part=2)
