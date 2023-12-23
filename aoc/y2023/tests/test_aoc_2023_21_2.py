from aoc.y2023.aoc_2023_21_2 import calculate_reached_garden_plots, the_map
from pytest import mark, param


@mark.parametrize(
    argnames=["steps", "expected"],
    argvalues=[
        param(
            6,
            16,
            id="In exactly 6 steps, he can still reach 16 garden plots.",
        ),
        param(
            10,
            50,
            id="In exactly 10 steps, he can reach any of 50 garden plots.",
        ),
        param(
            50,
            1594,
            id="In exactly 50 steps, he can reach 1594 garden plots.",
        ),
        param(
            100,
            6536,
            id="In exactly 100 steps, he can reach 6536 garden plots.",
        ),
        param(
            500,
            167004,
            id="In exactly 500 steps, he can reach 167004 garden plots.",
        ),
        param(
            1000,
            668697,
            id="In exactly 1000 steps, he can reach 668697 garden plots.",
        ),
        param(
            5000,
            16733044,
            id="In exactly 5000 steps, he can reach 16733044 garden plots.",
        ),
    ],
)
def test_that_example_numbers_are_calculated(steps: int, expected: int):
    actual = calculate_reached_garden_plots(terrain=the_map, steps=steps)
    assert expected == actual
