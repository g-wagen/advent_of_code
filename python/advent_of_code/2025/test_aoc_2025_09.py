import pytest
from aoc_2025_09 import calc_area

@pytest.mark.parametrize(
    argnames=["point1", "point2", "expected"],
    argvalues=[
        pytest.param([2, 5], [9, 7], 24),
        pytest.param([7, 1], [11, 7], 35),
        pytest.param([7, 3], [2, 3], 6),
        pytest.param([2, 5], [11, 1], 50),
    ],
)
def test_calc_area(point1, point2, expected):
    actual = calc_area(point1, point2)
    assert actual == expected
