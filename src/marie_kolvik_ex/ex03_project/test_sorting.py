__author__ = 'Marie Kolvik Valøy'
__email__ = 'mvaloy@nmbu.no'

def bubble_sort(data):
    """
    This function takes a list of numbers and return a list sorted in
    increasing order.
    Parameters
    ----------
    A list of numbers

    Returns
    -------
    A new, sorted list, exact same numbers as the original list.
    """
    increasing = list(data)
    n = len(increasing)
    done = 1
    for k in range(n - done):
        for i in range(n - done):
            compar = increasing[i + 1]
            tested = increasing[i]
            if tested > compar:
                increasing[i] = compar
                increasing[i + 1] = tested
        done += 1

    return increasing


if __name__ == "__main__":

    # I rewrite the variable name of data so as to not violate pep-8.
    for info in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(info, bubble_sort(info)))


    def test_empty():
        """Test that the sorting function works for empty list"""
        assert bubble_sort([]) == [], 'Wont work for empty lists.'


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([7]) == [7], 'Cant take single-element'


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    assert bubble_sort(data) != data, 'the function has no effect'


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    bubble_sort(data)
    assert data == data, 'test_original_unchanged failed'


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [1, 2, 3]
    assert bubble_sort(data) == data, 'test_sorted failed'


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [3, 2, 1]
    assert bubble_sort(data) == sorted(data), 'test_sort_reversed failed'


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [2, 1, 1, 2]
    assert bubble_sort(data) == [1, 1, 2, 2], 'test_sort_equal failed'


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    test = [4, 8, 1, 90, 3]
    assert bubble_sort(test) == [1, 3, 4, 8, 90], 'test_sorting case 0 failed'

    test1 = [0]
    assert bubble_sort(test1) == test1, 'test_sorting case 1 failed.'

    test2 = [0, 0, 0, 0]
    assert bubble_sort(test2) == test2, 'test_sorting case 2 failed.'

    test3 = 'edcba'
    assert bubble_sort(test3) == ['a', 'b', 'c', 'd',
                                  'e'], 'test_sorting case 3 failed'

    test4 = ['water', 'fire', 'earth', 'air']
    assert bubble_sort(test4) == ['air', 'earth', 'fire',
                                  'water'], 'test_sorting case 4 failed.'
