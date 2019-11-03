# -*- coding: utf-8 -*-

__author__ = 'Marie Kolvik Valøy'
__email__ = 'mvaloy@nmbu.no'


class LCGRand:
    slope = 7 ** 5
    congruence_class = 2 ** 31 - 1

    def __init__(self, seed):
        """
            Initialise a linear congruence random number generator

            Arguments
            ---------
            seed : int
                The initial seed for the generator
        """
        self.hidden_state = seed

    def rand(self):
        """
        Generate a single random number.

        Returns
        -------
        int
        A random integer
        """
        self.hidden_state = (
                    self.slope * self.hidden_state % self.congruence_class)
        return self.hidden_state

    def random_sequence(self, length):
        return RandIter(self, length)


class RandIter:
    def __init__(self, random_number_generator, length):
        """
        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate
        """
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        if self.num_generated_numbers is not None:
            raise RuntimeError(
                'You called __iter__ twice for the same RandIter object')
        else:
            self.num_generated_numbers = 0
            return self

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.
        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        """
        hiden_seed = 12
        if self.num_generated_numbers == self.length:
            raise StopIteration
        elif self.num_generated_numbers is None:
            raise RuntimeError('You must call __iter__ before __next__')
        else:
            return LCGRand(hiden_seed)

    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int
            A random number.
        """
        length = self.length
        hidden_seed = 3
        for it in range(length):
            self.length += 1
            return LCGRand(hidden_seed)
