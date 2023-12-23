from aoc.helper import choose_puzzle_input, print_solution

puzzle_input = choose_puzzle_input(
    y=2022,
    d=7,
    # sample_input_path="aoc_2022_07_input_sample.txt",
)

current_dir = []
directories = {}

for line in puzzle_input:
    splitline = line.split(" ")
    if splitline[0] == "$":
        splitline = splitline[1:]

    if splitline[0] == "ls" or line.startswith("dir"):
        continue

    if splitline[0].isnumeric():
        filesize = int(splitline[0])
        try:
            directories["/".join(current_dir)] += filesize
        except:
            directories["/".join(current_dir)] = filesize

    if splitline[0] == "cd":
        if splitline[1] == "..":
            current_dir.pop()
        elif splitline[1] == "/":
            current_dir = ["root"]
        else:
            nextdir = splitline[1]
            current_dir.append(nextdir)


folders_and_subfolders = {}

dirs_and_sizes = {}

for path, size in directories.items():
    new_parts = path.split("/")
    new_path = []

    for i in range(len(new_parts)):
        new_path.append(new_parts[i])
        joined_path = "/".join(new_path)
        try:
            dirs_and_sizes[joined_path].append(size)
        except:
            dirs_and_sizes[joined_path] = [size]


total_part1 = 0
for d, s in dirs_and_sizes.items():
    the_sum = sum(s)
    if the_sum <= 100000:
        total_part1 += the_sum

print_solution(total_part1, y=2022, d=7, part=1)

total_disk_space = 70000000
needed_disk_space_for_update = 30000000
used_disk_space = sum(dirs_and_sizes["root"])
too_big_by_this_much = abs(
    total_disk_space - needed_disk_space_for_update - used_disk_space
)

summed_dirs_and_sizes = {}
for d, s in dirs_and_sizes.items():
    summed_dirs_and_sizes[d] = sum(s)

summed_dirs_and_sizes = dict(
    sorted(summed_dirs_and_sizes.items(), key=lambda x: x[1])
)

for k, v in summed_dirs_and_sizes.items():
    if v >= too_big_by_this_much:
        print_solution(v, y=2022, d=7, part=2)
        break
