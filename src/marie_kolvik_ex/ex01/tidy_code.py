__author__ = 'Marie K. Valøy'
__email__ = 'mvaloy@nmbu.no'

from random import randint as a


def b():
    """
    Asks for a guess, tests if this is an integer of more than 1, if so,
    it returns c, if not it ask once more.
    """
    c = 0
    while c < 1:
        c = int(input('Your guess: '))
    return c


def d():
    """
    Simulating of throwing two dices and sum the numbers.
    Summing two random numbers between 1 and 6, including 1 and 6.
    """
    return a(1, 6) + a(1, 6)


def e(f, g):
    """ Checks if f is equal to g, if so it returns true, else it returns
    false.
    """
    return f == g


if __name__ == '__main__':

    h = False
    i = 3  # Number of guesses
    j = d()  # The throw
    while not h and i > 0:
        k = b()  # Guessed number
        h = e(j, k)  # Testing if your guess is correct
        if not h:
            print('Wrong, try again!')
            i -= 1  # One guess used

    if i > 0:
        print('You won {} points.'.format(i))
    else:
        print('You lost. Correct answer: {}.'.format(j))
