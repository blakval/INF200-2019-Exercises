__author__ = 'Marie Kolvik Valøy'
__email__ = 'mvaloy@nmbu.no'

import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data

    Source:
    https://github.com/yngvem/INF200-2019-Exercises/blob/master/
    exersices/ex03.rst

    With some modifying by me.
    """

    sorted_data = sorted(data)
    num_elements = len(sorted_data)

    if num_elements == 0:
        raise ValueError
    else:
        if num_elements % 2 == 1:
            return sorted_data[num_elements//2]
        else:
            return 0.5 * (sorted_data[num_elements//2 - 1] +
                          sorted_data[num_elements//2])


def test_median_single():
    """Tests that median returns correct value for an one-element list."""
    assert median([5]) == 5, 'Function failed test_median_single.'


def test_median_odd():
    """Tests that median works for lists with odd numbers of elements"""
    assert median([4, 6, 7]) == 6, 'Function failed test_median_odd.'


def test_median_even():
    """Tests that median works for lists with even numbers of elements"""
    assert median([4, 6, 7, 1000]) == 6.5, 'Function failed test_median_even.'


def test_median_sorted():
    """Tests if median works for lists with ordered elements"""
    assert median([1, 2, 3, 4, 5]) == 3, 'Function failed test_media_sorted.'


def test_median_reverse():
    """Tests if median works for lists with reverse-ordered elements"""
    assert median([5, 4, 3, 2, 1]) == 3, 'Function failed test_median_reverse.'


def test_median_unordered():
    """Tests if median works for unordered lists"""
    assert median([9, 1, 16, 0.3]) == 5, 'Failed test_median_unordered.'


def test_median_empty_raises_value_error():
    """Tests if the median raises a ValueError if given an empty list."""
    with pytest.raises(ValueError):
        median([])
