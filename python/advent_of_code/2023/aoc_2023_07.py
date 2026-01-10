from advent_of_code.helper import read_puzzle_input, print_solution
from copy import copy

year = 2023
day = 7

puzzle_input = read_puzzle_input(input_path=f"aoc_{year}_{day:02d}_input.txt")


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


def relative_hand_strength(hand: str, strength_map: dict) -> str:
    relative_strength = ""
    for card in hand:
        relative_strength += strength_map[card]
    return relative_strength



def generate_cards_counter(cards_in_hand: str) -> dict:
    my_cards_counter = {
        5: 0,
        4: 0,
        3: 0,
        2: 0,
        1: 0,
    }
    unique_cards = ""

    for card in cards_in_hand:
        if unique_cards.find(card) == -1:
            unique_cards += card

    for ucard in unique_cards:
        amount = cards_in_hand.count(ucard)
        my_cards_counter[amount] += 1

    return my_cards_counter




def rank(my_cards_counter: dict) -> int:
    if my_cards_counter[5] == 1:
        type_ = 1  # "Five of a kind"
    elif my_cards_counter[4] == 1:
        type_ = 2  # "Four of a kind"
    elif my_cards_counter[3] == 1 and my_cards_counter[2] == 1:
        type_ = 3  # "Full house"
    elif my_cards_counter[3] == 1 and my_cards_counter[1] == 2:
        type_ = 4  # "Three of a kind"
    elif my_cards_counter[2] == 2:
        type_ = 5  # "Two pair"
    elif my_cards_counter[2] == 1 and my_cards_counter[1] == 3:
        type_ = 6  # "One pair"
    else:
        type_ = 7  # "High card"

    return type_


def adjust_cards_counter_for_j2(
    cards_on_hand: str, cards_counter: dict
) -> dict:
    """This "if" monstrosity is horrible and should be fixed!"""
    my_cards_counter = copy(cards_counter)

    j_count = cards_on_hand.count("J")

    if j_count > 5:
        raise ValueError("There can't be more than 5 J's!")

    if j_count == len(cards_on_hand) or j_count == 0:
        return my_cards_counter

    elif j_count == 4:
        my_cards_counter[5] = 1
        my_cards_counter[4] = 0
        my_cards_counter[1] = 0

    elif j_count == 3:
        my_cards_counter[3] = 0
        if my_cards_counter[2] == 1:
            my_cards_counter[5] = 1
            my_cards_counter[2] = 0
        elif my_cards_counter[1] == 2:
            my_cards_counter[4] = 1
            my_cards_counter[1] = 1

    elif j_count == 2:
        my_cards_counter[2] -= 1
        if my_cards_counter[3] == 1:
            my_cards_counter[5] = 1
            my_cards_counter[3] = 0
            my_cards_counter[2] = 0
        elif my_cards_counter[2] == 1:
            my_cards_counter[4] = 1
            my_cards_counter[3] = 0
            my_cards_counter[2] = 0
        elif my_cards_counter[1] == 3:
            my_cards_counter[3] = 1
            my_cards_counter[1] -= 1

    elif j_count == 1:
        if my_cards_counter[4] == 1:
            my_cards_counter[5] = 1
            my_cards_counter[4] = 0
            my_cards_counter[1] = 0
        elif my_cards_counter[3] == 1:
            my_cards_counter[4] = 1
            my_cards_counter[3] = 0
            my_cards_counter[1] = 1
        elif my_cards_counter[2] == 2:
            my_cards_counter[3] = 1
            my_cards_counter[2] = 1
            my_cards_counter[1] = 0
        elif my_cards_counter[2] == 1:
            my_cards_counter[3] = 1
            my_cards_counter[2] = 0
            my_cards_counter[1] = 2
        elif my_cards_counter[1] == 5:
            my_cards_counter[2] = 1
            my_cards_counter[1] = 3
        elif my_cards_counter[1] == 4:
            raise Exception(
                "Can't have just 4 different cards without a fifth one!"
            )
        elif my_cards_counter[1] == 3:
            my_cards_counter[3] = 1
            my_cards_counter[2] = 0
            my_cards_counter[1] = 2
        elif my_cards_counter[1] == 2:
            my_cards_counter[4] = 1
            my_cards_counter[3] = 0
            my_cards_counter[1] = 1
        elif my_cards_counter[1] == 1:
            my_cards_counter[5] = 1
            my_cards_counter[4] = 0
            my_cards_counter[1] = 0

    return my_cards_counter


def adjust_cards_counter_for_j(cards_on_hand: str, cards_counter: dict) -> dict:
    """This "if" monstrosity is horrible and should be fixed!"""
    my_cards_counter = copy(cards_counter)

    j_count = cards_on_hand.count("J")

    if j_count > 5:
        raise Exception("There can't be more than 5 J's!")

    elif j_count == 5 or j_count == 0:
        return my_cards_counter

    elif j_count == 4:
        my_cards_counter[5] = 1
        my_cards_counter[4] = 0
        my_cards_counter[1] = 0

    elif j_count == 3:
        my_cards_counter[3] = 0
        if my_cards_counter[2] == 1:
            my_cards_counter[5] = 1
            my_cards_counter[2] = 0
        elif my_cards_counter[1] == 2:
            my_cards_counter[4] = 1
            my_cards_counter[1] = 1

    elif j_count == 2:
        my_cards_counter[2] -= 1
        if my_cards_counter[3] == 1:
            my_cards_counter[5] = 1
            my_cards_counter[3] = 0
            my_cards_counter[2] = 0
        elif my_cards_counter[2] == 1:
            my_cards_counter[4] = 1
            my_cards_counter[3] = 0
            my_cards_counter[2] = 0
        elif my_cards_counter[1] == 3:
            my_cards_counter[3] = 1
            my_cards_counter[1] -= 1

    elif j_count == 1:
        if my_cards_counter[4] == 1:
            my_cards_counter[5] = 1
            my_cards_counter[4] = 0
            my_cards_counter[1] = 0
        elif my_cards_counter[3] == 1:
            my_cards_counter[4] = 1
            my_cards_counter[3] = 0
            my_cards_counter[1] = 1
        elif my_cards_counter[2] == 2:
            my_cards_counter[3] = 1
            my_cards_counter[2] = 1
            my_cards_counter[1] = 0
        elif my_cards_counter[2] == 1:
            my_cards_counter[3] = 1
            my_cards_counter[2] = 0
            my_cards_counter[1] = 2
        elif my_cards_counter[1] == 5:
            my_cards_counter[2] = 1
            my_cards_counter[1] = 3
        elif my_cards_counter[1] == 4:
            raise Exception(
                "Can't have just 4 different cards without a fifth one!"
            )
        elif my_cards_counter[1] == 3:
            my_cards_counter[3] = 1
            my_cards_counter[2] = 0
            my_cards_counter[1] = 2
        elif my_cards_counter[1] == 2:
            my_cards_counter[4] = 1
            my_cards_counter[3] = 0
            my_cards_counter[1] = 1
        elif my_cards_counter[1] == 1:
            my_cards_counter[5] = 1
            my_cards_counter[4] = 0
            my_cards_counter[1] = 0

    return my_cards_counter


def y2023d7p1():
    cards_and_values_and_such = []

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

    for line in puzzle_input:
        hand, bid = line.split()
        cards_and_values_and_such.append(
            {
                "hand": hand,
                "strength": f"{hand_type(hand)}{relative_hand_strength(hand, strength_map)}",
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

    return total_winnings

def y2023d7p2():
    cards_and_values_and_such = []

    strength_map = {
        "A": "a",
        "K": "b",
        "Q": "c",
        "T": "e",
        "9": "f",
        "8": "g",
        "7": "h",
        "6": "i",
        "5": "j",
        "4": "k",
        "3": "l",
        "2": "m",
        "J": "z",
    }

    for line in puzzle_input:
        hand, bid = line.split()
        cards_counter = generate_cards_counter(hand)
        original_card_rank = rank(cards_counter)
        j_adjust = adjust_cards_counter_for_j2(hand, cards_counter)
        new_rank = rank(j_adjust)

        cards_and_values_and_such.append(
            {
                "strength": f"{new_rank}{relative_hand_strength(hand, strength_map)}",
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

    return total_winnings


print_solution(solution=y2023d7p1, y=year, d=day, part=1)

print_solution(solution=y2023d7p2, y=year, d=day, part=2)