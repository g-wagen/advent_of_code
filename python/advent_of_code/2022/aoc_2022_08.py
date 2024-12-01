from advent_of_code.helper import get_puzzle_input, print_solution
import numpy as np

puzzle_input = get_puzzle_input(y=2022, d=8)

make_grid: np.array = np.array([[y for y in x] for x in puzzle_input]).astype(
    int
)


def is_visible(number, coords: list):
    row = make_grid[coords[0], :]
    col = make_grid[:, coords[1]]
    left = all(number > row[: coords[1]])
    right = all(number > row[coords[1] + 1 :])
    above = all(number > col[: coords[0]])
    below = all(number > col[coords[0] + 1 :])

    return any([left, right, above, below])


border_trees = (make_grid.shape[0] * 2) + ((make_grid.shape[1] - 2) * 2)
visible_counter = border_trees

for idx, x in np.ndenumerate(make_grid):
    # don't check outer border visibilities.
    # these are already calculated
    if (
        0 < idx[0] < make_grid.shape[0] - 1
        and 0 < idx[1] < make_grid.shape[1] - 1
    ):
        if is_visible(x, idx):
            visible_counter += 1

print_solution(visible_counter, 2022, 8, 1)

highest_rating = 0


def calculate_dir_score(cur, dir):
    out = 0
    for i in [cur <= x for x in dir]:
        out += 1
        if i:
            break
    return out


def calculate_scenic_score(tree_coords, grid):
    current = grid[tree_coords]
    x = tree_coords[1]
    y = tree_coords[0]
    above = grid[:y, x][::-1]
    below = grid[y + 1 :, x]
    left = grid[y, :x][::-1]
    right = grid[y, x + 1 :]
    above_score = calculate_dir_score(current, above)
    below_score = calculate_dir_score(current, below)
    left_score = calculate_dir_score(current, left)
    right_score = calculate_dir_score(current, right)

    return above_score * below_score * left_score * right_score


for idx, x in np.ndenumerate(make_grid):
    scenic_score = calculate_scenic_score(tree_coords=idx, grid=make_grid)
    if scenic_score > highest_rating:
        highest_rating = scenic_score

print_solution(highest_rating, 2022, 8, 2)
