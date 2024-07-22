import pytest
import rare_dif


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0),
    (1, 2, -1),
    (2, 1, 1),
    (2, 2, 0),
    (0, 0, 0),
    (-1, -1, 0),
    (10, -1, 11),
])
def test_minus(a, b, expected):
    assert rare_dif.example.minus.minus(a, b) == expected
