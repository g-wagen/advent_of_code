from helper import get_puzzle_input
from random import choice

puzzle_input = get_puzzle_input(y=2021, d=12)


class CavePath:
    def __init__(self, data: str) -> None:
        split_data: list = data.split('-')
        self.start: str = split_data[0]
        self.end: str = split_data[1]
        self.members: list = [self.start, self.end]


class CaveSystem:
    def __init__(self, input_data: list[str]) -> None:
        self.cave_paths = [CavePath(data=x) for x in input_data]

        self.small_caves = set()
        self.big_caves = set()

        for path in self.cave_paths:
            self.small_caves.add(path.start) if path.start.islower() else self.big_caves.add(path.start)
            self.big_caves.add(path.end) if path.end.isupper() else self.small_caves.add(path.end)

        self.small_caves_visit_counter = {c: 1 for c in self.small_caves}

    def all_caves(self):
        caves = []
        for path in self.cave_paths:
            caves.append(path.start)
            caves.append(path.end)

        caves = list(set(caves))

        return caves

    def adjacent(self, cave: str):
        adj = set()
        for cp in self.cave_paths:
            if cave in cp.members:
                adj.add(cp.start)
                adj.add(cp.end)

        adj.discard(cave)

        return list(adj)

    def go(self, start):
        connections = self.adjacent(start)
        choose_next = choice(connections)
        if choose_next in self.big_caves:
            self.go(choose_next)
        elif choose_next in self.small_caves:
            if self.small_caves_visit_counter[choose_next] > 0:
                self.go(choose_next)
                self.small_caves_visit_counter[choose_next] -= 1
            else:
                ...
        elif choose_next == 'end':

    def dont_go(self, choices):
        next


cave_system = CaveSystem(input_data=puzzle_input)
print(cave_system.all_caves())
print(cave_system.adjacent('ZH'))
print(cave_system.small_caves_visit_counter)
print(cave_system.big_caves)
