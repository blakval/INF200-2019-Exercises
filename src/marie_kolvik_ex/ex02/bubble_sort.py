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

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
