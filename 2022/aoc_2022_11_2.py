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
            operand = item if self.operand == "same" else self.operand

            the_item = int(item)
            the_operand = int(operand)

            if self.operator == "*":
                worry_level = the_item * the_operand
            if self.operator == "+":
                worry_level = the_item + the_operand

            bored_level = worry_level % factor

            if bored_level % self.test_value == 0:
                self.monkey_true.items.append(bored_level)
            else:
                self.monkey_false.items.append(bored_level)

        self.items = []

    def set_monkey_true(self, monkey):
        self.monkey_true = monkey

    def set_monkey_false(self, monkey):
        self.monkey_false = monkey


monkey0 = Monkey(items=[89, 74], operator="*", operand=5, test_value=17)
monkey1 = Monkey(
    items=[75, 69, 87, 57, 84, 90, 66, 50], operator="+", operand=3, test_value=7
)
monkey2 = Monkey(items=[55], operator="+", operand=7, test_value=13)
monkey3 = Monkey(items=[69, 82, 69, 56, 68], operator="+", operand=5, test_value=2)
monkey4 = Monkey(items=[72, 97, 50], operator="+", operand=2, test_value=19)
monkey5 = Monkey(items=[90, 84, 56, 92, 91, 91], operator="*", operand=19, test_value=3)
monkey6 = Monkey(items=[63, 93, 55, 53], operator="*", operand="same", test_value=5)
monkey7 = Monkey(
    items=[50, 61, 52, 58, 86, 68, 97], operator="+", operand=4, test_value=11
)

monkey0.set_monkey_true(monkey4)
monkey0.set_monkey_false(monkey7)

monkey1.set_monkey_true(monkey3)
monkey1.set_monkey_false(monkey2)

monkey2.set_monkey_true(monkey0)
monkey2.set_monkey_false(monkey7)

monkey3.set_monkey_true(monkey0)
monkey3.set_monkey_false(monkey2)

monkey4.set_monkey_true(monkey6)
monkey4.set_monkey_false(monkey5)

monkey5.set_monkey_true(monkey6)
monkey5.set_monkey_false(monkey1)

monkey6.set_monkey_true(monkey3)
monkey6.set_monkey_false(monkey1)

monkey7.set_monkey_true(monkey5)
monkey7.set_monkey_false(monkey4)

rounds = 10000
monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]


for i in range(rounds):
    worry_factor = np.prod([monkey.test_value for monkey in monkeys])
    print(f"{i} of {rounds}")

    for m in monkeys:
        m.business(worry_factor)

monkey_business = []
for i, m in enumerate(monkeys):
    monkey_business.append(m.inspection_counter)
    print(i, f"Monkey {i} inspected items {m.inspection_counter} times", m.items)

solution = np.product(sorted(monkey_business)[-2:])

print_solution(solution, y=2022, d=11, part=2)
