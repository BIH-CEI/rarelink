import numpy as np
import pytest

import rare_dif


@pytest.mark.parametrize("arr, expected", [
    (np.array([1, 1, 1]), 3),
    (np.array([1, 2, 3]), 6),
    (np.array([2, 1, -3]), 0),
    ([1, 1, 1], 3),
    ([1, 2, 3], 6),
    ([2, 1, -3], 0),
])
def test_sum_over_array(arr, expected):
    assert rare_dif.numpy_example.sum_over_array.sum_over_array(arr) == expected
