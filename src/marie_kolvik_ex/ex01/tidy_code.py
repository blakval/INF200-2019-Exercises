__author__ = 'Marie K. Valøy'
__email__ = 'mvaloy@nmbu.no'

from random import randint


def ask_for_guess():
    """
    Asks for a guess, tests if this is an positive integer, if so,
    it returns c, if not it ask once more.
    """
    guessed = 0
    while guessed < 1:
        guessed = int(input('Your guess: '))
    return guessed


def sum_of_dices():
    """
    Simulation of throwing two dices and sum the numbers.
    Summing two random numbers between 1 and 6, including 1 and 6.
    """
    return randint(1, 6) + randint(1, 6)


def is_equal(throw, guess):
    """
    Checks if f is equal to g, if so it returns true, else it returns
    false.
    """
    return throw == guess


if __name__ == '__main__':

    Test = False
    number_of_guesses = 3
    Throw = sum_of_dices()

    while not Test and number_of_guesses > 0:
        your_guess = ask_for_guess()
        Test = is_equal(Throw, your_guess)

        if not Test:
            print('Wrong, try again!')
            number_of_guesses -= 1  # One guess used

    if number_of_guesses > 0:
        print('You won {} points.'.format(number_of_guesses))
    else:
        print('You lost. Correct answer: {}.'.format(Throw))
