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


