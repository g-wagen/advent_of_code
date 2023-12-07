from helper import choose_puzzle_input, print_solution

year = 2023
day = 7

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)

strength_map = {
    "A": "a",
    "K": "b",
    "Q": "c",
    "J": "d",
    "T": "e",
    "9": "f",
    "8": "g",
    "7": "h",
    "6": "i",
    "5": "j",
    "4": "k",
    "3": "l",
    "2": "m",
}

# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456


def hand_type(hand: str) -> int:
    type_ = -1

    cards = {
        5: 0,
        4: 0,
        3: 0,
        2: 0,
        1: 0,
    }
    unique_cards = ""
    for card in hand:
        if unique_cards.find(card) == -1:
            unique_cards += card

    for ucard in unique_cards:
        amount = hand.count(ucard)
        cards[amount] += 1

    if cards[5] == 1:
        type_ = 1
    elif cards[4] == 1:
        type_ = 2
    elif cards[3] == 1 and cards[2] == 1:
        type_ = 3
    elif cards[3] == 1 and cards[1] == 2:
        type_ = 4
    elif cards[2] == 2:
        type_ = 5
    elif cards[2] == 1 and cards[1] == 3:
        type_ = 6
    else:
        type_ = 7

    return type_


def relative_hand_strength(hand: str) -> str:
    relative_strength = ""
    for card in hand:
        relative_strength += strength_map[card]
    return relative_strength


cards_and_values_and_such = []

for line in puzzle_input:
    hand, bid = line.split()
    cards_and_values_and_such.append(
        {
            "hand": hand,
            "strength": f"{hand_type(hand)}{relative_hand_strength(hand)}",
            "bid": int(bid),
        }
    )

total_winnings = 0

for i, item in enumerate(
    sorted(
        cards_and_values_and_such,
        reverse=True,
        key=lambda x: x["strength"],
    )
):
    total_winnings += item["bid"] * (i + 1)

print_solution(solution=total_winnings, y=year, d=day, part=1)
