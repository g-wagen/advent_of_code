from copy import copy

from advent_of_code.helper import choose_puzzle_input, print_solution

year = 2023
day = 7

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


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


def convert_j_cards(cards_in_hand: str) -> str:
    j_count = cards_in_hand.find("J")

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
    strength = "".join([strength_map[c] for c in cards_in_hand])

    cards = {}
    for card in cards_in_hand:
        if cards.get(card):
            cards[card] += 1
        else:
            cards[card] = 1

    sorted_cards = {}
    for k, v in strength_map.items():
        if cards.get(k):
            sorted_cards[k] = cards[k]

    print(sorted_cards)

    if j_count > 0:
        del sorted_cards["J"]
        most_frequent = sorted(
            sorted_cards.items(), reverse=True, key=lambda x: x[1]
        )[0][0]

        sorted_cards[most_frequent] += j_count
        print(sorted_cards[most_frequent])

    output = cards_in_hand

    # if j_count > 0:
    #     temp = output.replace("J", "")
    #     output = output.replace("J", min(temp))

    # print(cards_in_hand, strength)

    # print(most_frequent)

    # cards[0] = (cards[0][0], cards[0][1] + j_count)

    # temp = ""
    # for k, v in dict(cards).items():
    #     for i in range(v):
    #         temp += k
    # sorto = {k: cards[k] for k in cards.keys() if k in cards}
    # print(sorto)
    #
    # return cards, cards_in_hand, output, strength, temp


print("32TAK", convert_j_cards("32TAK"))
print("JJJAT", convert_j_cards("JJJAT"))
print("KJJJT", convert_j_cards("KJJJT"))

#
# for k, v in my_cards_counter.items():
#     if v > 0:
#         break
#
# return my_cards_counter


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


def relative_hand_strength(hand: str) -> str:
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
    relative_strength = ""
    for card in hand:
        relative_strength += strength_map[card]

    return relative_strength


cards_and_values_and_such = []

for line in puzzle_input:
    hand, bid = line.split()
    cards_counter = generate_cards_counter(hand)
    original_card_rank = rank(cards_counter)
    j_adjust = adjust_cards_counter_for_j2(hand, cards_counter)
    new_rank = rank(j_adjust)

    cards_and_values_and_such.append({
        "strength": f"{new_rank}{relative_hand_strength(hand)}",
        "bid": int(bid),
    })

total_winnings = 0

for i, item in enumerate(
    sorted(
        cards_and_values_and_such,
        reverse=True,
        key=lambda x: x["strength"],
    )
):
    total_winnings += item["bid"] * (i + 1)

print_solution(solution=total_winnings, y=year, d=day, part=2)
