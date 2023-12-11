from helper import choose_puzzle_input, print_solution

year = 2023
day = 11

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)

vertical_expansion = []

# vertical expansion
for line in puzzle_input:
    galaxies = line.find("#")
    vertical_expansion.append(line)
    if galaxies < 0:
        vertical_expansion.append(line)


vertical_galaxy_counter = []
for i, column in enumerate(vertical_expansion[0]):
    galaxy_counter = 0
    for row in range(len(vertical_expansion)):
        if vertical_expansion[row][i] == "#":
            galaxy_counter += 1

    vertical_galaxy_counter.append(galaxy_counter)

horizontal_expansion = []

for row in vertical_expansion:
    expanded_horizontal_row = ""
    for x, column in enumerate(row):
        expanded_horizontal_row += column
        if vertical_galaxy_counter[x] == 0:
            expanded_horizontal_row += column
    horizontal_expansion.append(expanded_horizontal_row)

print("\n".join(horizontal_expansion))
print(len(horizontal_expansion[0]))
galaxy_coordinates = []
for y, row in enumerate(horizontal_expansion):
    for x, column in enumerate(row):
        if column == "#":
            galaxy_coordinates.append([y, x])

print(galaxy_coordinates)


print_solution(solution=0, y=year, d=day, part=1)


print_solution(solution=0, y=year, d=day, part=2)
