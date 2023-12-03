from typing import Union
from helper import choose_puzzle_input, print_solution

year = 2023
day = 3

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


# 1. input als 2d liste speichern  v/
# 2. zahlen zu int konvertieren  v/
# 3. alle symbole finden und index speichern  v/
# 4. durch symbole iterieren:
#   - in koordinaten schauen ob da zahlen stehen (diagonal senkrecht, vertikal)
#       - U
#       - UR
#       - R
#       - DR
#       - D
#       - DL
#       - L
#       - UL
# 5. Wenn zahl gefunden:
#       - U: 1. ab X index von U in oberer zeile iterieren iterieren bis keine zahl mehr
#            und in list/deque appenden
#            1. ab X-1 index von U in oberer Zeile rückwärts iterieren bis keine Zahl und
#            an andere liste appenden
#            3. neue liste aus umgedrehter zweiter liste + erster liste
#            4. nummer als Part Nummer an part nummer liste anfügen

symbols = []
part_numbers = []
schematic = []

part_number_chars = ""


# puzzle_input = [
#     '.........',
#     '.360*201.',
#     '.........'
# ]

for y, line in enumerate(puzzle_input):
    # print(line)
    temp_list = []
    for x, char in enumerate(line):
        if char.isnumeric():
            temp_list.append(char)
        elif char == ".":
            temp_list.append(" ")
        else:
            temp_list.append(char)
            symbols.append([char, y, x])
            if char not in part_number_chars:
                part_number_chars += char

    schematic.append(temp_list)

print(part_number_chars)


def lowest_index(input_list: list[list], the_line: str, funky_chars: str):
    lowest = len(input_list[0])
    for char in funky_chars:
        char_id = the_line.find(char)
        if char_id < 0:
            continue
        elif char_id < lowest:
            lowest = char_id
    return lowest


def read_from_index(input_array: list[list], y: int, x: int):
    cur_line = "".join(input_array[y])

    forward_line = cur_line[x:]
    backward_line = cur_line[:x][::-1]
    non_digit_chars = part_number_chars + " "

    # line beginning
    forward_lowest = lowest_index(
        input_list=input_array,
        the_line=forward_line,
        funky_chars=non_digit_chars,
    )

    beginning = forward_line[:forward_lowest]

    # line end
    backward_lowest = lowest_index(
        input_list=input_array,
        the_line=backward_line,
        funky_chars=non_digit_chars,
    )

    end = backward_line[:backward_lowest]

    if len(beginning) == 1:
        part_number = end[::-1] + beginning
    elif len(end) == 1:
        part_number = end + beginning
    else:
        part_number = beginning + end

    return int(part_number.strip())


adjacents = []
check_these = []
for s in symbols:
    sy = s[1]
    sx = s[2]

    u_y = sy - 1
    d_y = sy + 1
    r_x = sx + 1
    l_x = sx - 1

    # for direction in [
    #     [u_y, sx],
    #     [u_y, r_x],
    #     [sy, r_x],
    #     [d_y, r_x],
    #     [d_y, sx],
    #     [d_y, l_x],
    #     [sy, l_x],
    #     [u_y, l_x],
    # ]:
    #     try:
    #         content = schematic[direction[0]][direction[1]]
    #         if content.isnumeric():
    #             check_these.append([content[0], content[1]])
    #     except:
    #         content = None
    try:
        u = schematic[u_y][sx]
        if u.isnumeric():
            check_these.append([u_y, sx])
    except IndexError:
        u = None
    try:
        ur = schematic[u_y][r_x]
        if ur.isnumeric():
            check_these.append([u_y, r_x])
    except IndexError:
        ur = None
    try:
        r = schematic[sy][r_x]
        if r.isnumeric():
            check_these.append([sy, r_x])
    except IndexError:
        r = None
    try:
        dr = schematic[d_y][r_x]
        if dr.isnumeric():
            check_these.append([d_y, r_x])
    except IndexError:
        dr = None
    try:
        d = schematic[d_y][sx]
        if d.isnumeric():
            check_these.append([d_y, sx])
    except IndexError:
        d = None
    try:
        dl = schematic[d_y][l_x]
        if dl.isnumeric():
            check_these.append([d_y, l_x])
    except IndexError:
        dl = None
    try:
        l = schematic[sy][l_x]
        if l.isnumeric():
            check_these.append([sy, l_x])
    except IndexError:
        l = None
    try:
        ul = schematic[u_y][l_x]
        if ul.isnumeric():
            check_these.append([u_y, l_x])
    except IndexError:
        ul = None

print(check_these)

for sch in schematic:
    print(sch)


# for i in [
#     [0, 2, 467],
#     [0, 0, 467],
#     [0, 1, 467],
#     [2, 2, 35],
#     [2, 3, 35],
#     [2, 6, 633],
#     [2, 7, 633],
#     [2, 8, 633],
#     [4, 0, 617],
#     [4, 1, 617],
#     [4, 2, 617],
#     [6, 2, 592],
#     [6, 3, 592],
#     [6, 4, 592],
#     [7, 6, 755],
#     [7, 7, 755],
#     [7, 8, 755],
#     [9, 1, 664],
#     [9, 2, 664],
#     [9, 3, 664],
#     [9, 5, 598],
#     [9, 6, 598],
#     [9, 7, 598],
# ]:
#     result = read_from_index(input_array=schematic, y=i[0], x=i[1])
#     print("TEST", i[2], result, i[2] == result)

part_numbers = []
for p in part_numbers:
    print(p)

for coords in check_these:
    part_numbers.append(
        read_from_index(input_array=schematic, y=coords[0], x=coords[1])
    )


print_solution(solution=sum(list(set(part_numbers))), y=year, d=day, part=1)
# LOW:  336560
# HIGH: 847901
print_solution(solution=0, y=year, d=day, part=2)
