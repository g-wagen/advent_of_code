from advent_of_code import helper

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


for item in data:
    stack = []
    stop = False
    for i, c in enumerate(item):
        if c in opening:
            stack.append(c)
        else:
            char_index = closing.find(c)
            if stack[-1] == opening[char_index]:
                stack.pop()
            else:
                expected = closing.find(stack[-1])
                print(
                    f'{"".join(stack)} : Expected {closing[expected + 1]}, but found {c} instead!'
                )
                score.append(points[c])
                stop = True
        if stop:
            break

print(f"\nPuzzle answer: {sum(score)}")
