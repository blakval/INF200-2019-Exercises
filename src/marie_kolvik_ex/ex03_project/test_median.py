__author__ = 'Marie Kolvik Valøy'
__email__ = 'mvaloy@nmbu.no'


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data

    Source:
    https://github.com/yngvem/INF200-2019-Exercises/blob/master/
    exersices/ex03.rst
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
        else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


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
    """Tests if the median works for lists with ordered elements"""
    assert median([1, 2, 3, 4, 5]) == 3, 'Function failed thest_media_sorted.'


def test_median_reverse():
    """Tests if the median works for lists with reverse-ordered elements"""
    assert median([5, 4, 3, 2, 1]) == 3, 'Function failed test_median_reverse.'


def test_median_unordered():
    """Tests if the median works for unordered lists"""
    assert median([9, 1, 16, 0.3]) == 5, 'Failed test_median_unordered.'
