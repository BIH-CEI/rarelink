import typing

import numpy as np


def sum_over_array(arr: typing.Union[np.array, typing.List]) -> typing.Union[int, float]:
    """
    This function returns the sum of all elements in an array.

    very similar to :func:`np.sum` but written myself.

    :param arr: an array or a list
    :return: the sum of all elements in the array
    """
    arr_sum = 0
    for item in arr:
        arr_sum += item

    return arr_sum
