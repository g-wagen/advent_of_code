from helper import choose_puzzle_input, print_solution

year = 2023
day = 4

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)

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


print_solution(solution=sum(total_cards.values()), y=year, d=day, part=2)
