from aoc.helper import choose_puzzle_input, print_solution
import numpy as np

puzzle_input = choose_puzzle_input(
    y=2022,
    d=11,
    # sample_input_path="aoc_2022_11_inputsample.txt",
)


class Monkey:
    inspection_counter = 0

    def __init__(self, items: list, operator, operand, test_value):
        self.items = items
        self.test_value = test_value
        self.monkey_true = None
        self.monkey_false = None
        self.operand = operand
        self.operator = operator

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


puzzle_input = [x.strip() for x in puzzle_input if x]

monkeys_dict = {}
current_monkey_id = 0

for l in puzzle_input:
    if l.startswith("Monkey"):
        current_monkey_id = int(l.split()[-1].replace(":", ""))
        monkeys_dict[current_monkey_id] = {}
    elif l.startswith("Starting"):
        all_items = l.split(":")[-1]
        individual_items = all_items.split(",")
        monkeys_dict[current_monkey_id]["items"] = [
            int(item.strip()) for item in individual_items
        ]
    elif l.startswith("Operation"):
        _, operator, operand = l.split("=")[-1].split()
        monkeys_dict[current_monkey_id]["operator"] = operator
        monkeys_dict[current_monkey_id]["operand"] = (
            int(operand) if operand.isnumeric() else "same"
        )
    elif l.startswith("Test"):
        monkeys_dict[current_monkey_id]["test_value"] = int(
            l.split()[-1].strip()
        )
    elif l.startswith("If true"):
        monkeys_dict[current_monkey_id]["monkey_true"] = int(
            l.split()[-1].strip()
        )
    elif l.startswith("If false"):
        monkeys_dict[current_monkey_id]["monkey_false"] = int(
            l.split()[-1].strip()
        )


monkey_objects = {}

for monkey, attrs in monkeys_dict.items():
    monkey_objects[monkey] = Monkey(
        items=attrs["items"],
        operator=attrs["operator"],
        operand=attrs["operand"],
        test_value=attrs["test_value"],
    )

for (monkey, attrs), (monkey_obj, monkey_obj_attr) in zip(
    monkeys_dict.items(), monkey_objects.items()
):
    monkey_obj_attr.set_monkey_true(monkey_objects[attrs["monkey_true"]])
    monkey_obj_attr.set_monkey_false(monkey_objects[attrs["monkey_false"]])


rounds = 10000
for i in range(rounds):
    worry_factor = np.prod([
        monkey.test_value for k, monkey in monkey_objects.items()
    ])
    # print(f"{i} of {rounds}")

    for j, m in monkey_objects.items():
        m.business(worry_factor)

monkey_business = []
for i, (j, m) in enumerate(monkey_objects.items()):
    monkey_business.append(m.inspection_counter)
    print(f"Monkey {i} inspected items {m.inspection_counter} times.")

solution = np.product(sorted(monkey_business)[-2:])

print_solution(solution, y=2022, d=11, part=2)
