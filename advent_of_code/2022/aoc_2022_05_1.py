from advent_of_code.helper import get_puzzle_input

puzzle_input = get_puzzle_input(y=2022, d=5)

stacks = {
    1: ["R", "H", "M", "P", "Z"],
    2: ["B", "J", "C", "P"],
    3: ["D", "C", "L", "G", "H", "N", "S"],
    4: ["L", "R", "S", "Q", "D", "M", "T", "F"],
    5: ["M", "Z", "T", "B", "Q", "P", "S", "F"],
    6: ["G", "B", "Z", "S", "F", "T"],
    7: ["V", "R", "N"],
    8: ["M", "C", "V", "D", "T", "L", "G", "P"],
    9: ["L", "M", "F", "J", "N", "Q", "W"],
}


def read_instruction(data: str):
    data = data.split(" ")
    numbers = [int(x) for x in data if x.isdigit()]
    return numbers


instructions = [x for x in puzzle_input[10:] if len(x) > 0 or x != " "]


def execute_instruction(instruction: list):
    amount: int = instruction[0]
    from_stack: int = instruction[1]
    to_stack: int = instruction[2]

    reversed_from_stack: list = stacks.get(from_stack)
    reversed_from_stack.reverse()
    reversed_to_stack: list = stacks.get(to_stack)
    reversed_to_stack.reverse()

    for a in range(amount):
        reversed_to_stack.append(reversed_from_stack.pop())

    new_from_stack = reversed_from_stack[::-1]
    new_to_stack = reversed_to_stack[::-1]
    stacks[from_stack] = new_from_stack
    stacks[to_stack] = new_to_stack

    # return stacks


for i, instr in enumerate(instructions):
    print(instr)
    read = read_instruction(instr)
    print(read)
    # print(stacks)
    # try:
    execute_instruction(instruction=read)
    # except:
    #     pass

code = ""

for k, v in stacks.items():
    code += v[0]

print(code)
