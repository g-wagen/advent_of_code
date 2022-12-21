from helper import get_puzzle_input, print_solution
import numpy as np
import sys

# sys.set_int_max_str_digits(999999999)

# puzzle_input = get_puzzle_input(y=2022, d=11)
# with open('aoc_2022_11_inputsample.txt', 'r') as f:
#     puzzle_input = f.read().splitlines()


class Monkey:
    inspection_counter = 0

    def __init__(self, items: list, operator, operand, test_value):
        self.items = items
        self.test_value = test_value
        self.monkey_true = None
        self.monkey_false = None
        self.operand = operand
        self.operator = operator
        self.worry_level: int = 0

    def business(self, factor):
        for item in self.items:
            self.inspection_counter += 1
            operand = item if self.operand == 'same' else self.operand

            the_item = int(item)
            the_operand = int(operand)

            if self.operator == '*':
                worry_level = the_item * the_operand
            if self.operator == '+':
                worry_level = the_item + the_operand

            # bored_level = worry_level % 3
            # bored_level = worry_level // 3
            bored_level = worry_level % factor
            # self.worry_level = bored_level

            if bored_level % self.test_value == 0:
                self.monkey_true.items.append(bored_level)
            else:
                self.monkey_false.items.append(bored_level)

        self.items = []

    def set_monkey_true(self, monkey):
        self.monkey_true = monkey

    def set_monkey_false(self, monkey):
        self.monkey_false = monkey


monkey0 = Monkey(items=[79, 98], operator='*', operand=19, test_value=23)
monkey1 = Monkey(items=[54, 65, 75, 74], operator='+', operand=6, test_value=19)
monkey2 = Monkey(items=[79, 60, 97], operator='*', operand='same', test_value=13)
monkey3 = Monkey(items=[74], operator='+', operand=3, test_value=17)

monkey0.set_monkey_true(monkey2)
monkey0.set_monkey_false(monkey3)

monkey1.set_monkey_true(monkey2)
monkey1.set_monkey_false(monkey0)

monkey2.set_monkey_true(monkey1)
monkey2.set_monkey_false(monkey3)

monkey3.set_monkey_true(monkey0)
monkey3.set_monkey_false(monkey1)

rounds = 10000
rounds = 10000

monkeys = [monkey0, monkey1, monkey2, monkey3]


for i in range(rounds):
    worry_factor = np.prod([monkey.test_value for monkey in monkeys])
    print(f'{i} of {rounds}')

    for m in monkeys:
        m.business(worry_factor)
        # print(m.worry_level)

monkey_business = []
for i, m in enumerate(monkeys):
    monkey_business.append(m.inspection_counter)
    print(i, f'Monkey {i} inspected items {m.inspection_counter} times', m.items)

solution = np.product(sorted(monkey_business)[-2:])

print_solution(solution, y=2022, d=11, part=2)
