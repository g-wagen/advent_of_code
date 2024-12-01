from advent_of_code import helper
import numpy as np

data = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]

data = helper.get_puzzle_input(d=10, y=2021)
opening = "[({<"
closing = "])}>"

points = {"]": 57, ")": 3, "}": 1197, ">": 25137}
score = []

# find corrupt lines
corrupt_lines = []
for item in data:
    stack = []
    stop = False
    for i, c in enumerate(item):
        # add open char to stack
        if c in opening:
            stack.append(c)
        else:
            # close segment and remove open char from stack
            char_index = closing.find(c)
            if stack[-1] == opening[char_index]:
                stack.pop()
            # complain about broken sequence
            else:
                expected = closing.find(stack[-1]) + 1
                score.append(points[c])
                stop = True
        # remove broken sequence from data
        if stop:
            corrupt_lines.append(item)
            break

# delete corrupt lines
for corr in corrupt_lines:
    if corr in data:
        data.remove(corr)


points = {"]": 2, ")": 1, "}": 3, ">": 4}
score = []
for item in data:
    stack = []
    stop = False
    for i, c in enumerate(item):
        # add open char to stack
        if c in opening:
            stack.append(c)
        else:
            # close segment and remove open char from stack
            if stack[-1] == opening[closing.find(c)]:
                stack.pop()
            # complain about broken sequence
            else:
                stop = True
        # remove broken sequence from data
        if stop:
            break

    end_stack = ""
    for i, c in enumerate(stack[::-1]):
        end_stack += closing[opening.find(c)]

    tmp_score = 0
    for c in end_stack:
        tmp_score *= 5
        tmp_score += points[c]

    score.append(tmp_score)

# print(score)
print(f'Puzzle answer: {np.median(score).astype("int")}')
