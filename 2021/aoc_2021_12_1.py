from helper import get_puzzle_input
from random import choice

puzzle_input = get_puzzle_input(y=2021, d=12)
with open("aoc_2021_12_testinput.txt", "r") as f:
    puzzle_input = f.read().splitlines()


class CavePath:
    def __init__(self, data: str) -> None:
        split_data: list = data.split("-")
        self.start: str = split_data[0]
        self.end: str = split_data[1]
        self.members: list = [self.start, self.end]


class CaveSystem:
    def __init__(self, input_data: list[str]) -> None:
        self.cave_paths = [CavePath(data=x) for x in input_data]

        self.small_caves = set()
        self.big_caves = set()

        for path in self.cave_paths:
            self.small_caves.add(
                path.start
            ) if path.start.islower() else self.big_caves.add(path.start)
            self.big_caves.add(
                path.end
            ) if path.end.isupper() else self.small_caves.add(path.end)

        self.small_caves_visited = {c: False for c in self.small_caves}

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

    def random_cave(self, cave_list):
        return choice(cave_list)

    def traverse(self):
        possibilities = self.adjacent("start")
        for p in possibilities:
            print(p)

    def go(self, there):
        print(there)
        if there in self.small_caves and not self.small_caves_visited[there]:
            self.small_caves_visited[there] = True
            self.go(there)
        elif there in self.big_caves:
            self.go(there)
        elif there in self.small_caves and self.small_caves_visited[there]:
            self.go(choice(self.adjacent(there)))
        elif there == "end":
            return

    def no_go(self): ...

    # start
    # find neighbors
    # choose random neighbor:
    #   if end then stop
    #   else check neighbor:...
    # check neighbor:
    #   if big cave then go there and recurse
    #   if small cave check if visited:
    #       if not visited go there and recurse
    #       if visited go back and recurse

    def do_it(self, current, out: list):
        if current == "start":
            out.append("start")
        if current == "end":
            if "end" not in out:
                out.append("end")
            return out
        nearby = self.adjacent(current)
        if "start" in nearby:
            del nearby[nearby.index("start")]
        go_next = self.random_cave(nearby)
        if go_next in self.big_caves:
            out.append(go_next)
            self.do_it(go_next, out)
        if go_next in self.small_caves:
            if not self.small_caves_visited[go_next]:
                self.small_caves_visited[go_next] = True
                out.append(go_next)
                self.do_it(go_next, out)
            else:
                try:
                    del nearby[nearby.index(go_next)]
                    next_random = self.random_cave(nearby)
                    out.append(next_random)
                    self.do_it(next_random, out)
                except:
                    return out
        return out

    # def go(self, start):
    #     connections = self.adjacent(start)
    #     choose_next = choice(connections)
    #     print(choose_next)
    #     if choose_next in self.big_caves:
    #         self.go(choose_next)
    #     elif choose_next in self.small_caves:
    #         if not self.small_caves_visited[choose_next]:
    #             self.small_caves_visited[choose_next] = True
    #             self.go(choose_next)
    #         else:
    #             self.go(choice(connections))
    #     elif choose_next == 'end':
    #         return


solutions = set()

cave_system = CaveSystem(input_data=puzzle_input)
for i in range(1000):
    sol = []
    cave_system.do_it("start", sol)
    # if 'end' in sol:
    #     solutions.add(','.join(sol))

    lowercase_unique = []
    testing = {x for x in sol if x.islower()}

    for t in testing:
        if sol.count(t) == 1 and "end" in sol:
            solutions.add(",".join(sol))

print(len(set(solutions)))
[print(x) for x in set(solutions)]

# print(cave_system.all_caves())
# print(cave_system.adjacent('ZH'))
# print(cave_system.small_caves_visited)
# print(cave_system.big_caves)
