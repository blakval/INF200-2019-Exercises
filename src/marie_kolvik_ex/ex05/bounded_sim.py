# -*- coding: utf-8 -*-

__author__ = 'Marie Kolvik Valøy'
__email__ = 'mvaloy@nmbu.no'

from src.marie_kolvik_ex.ex05.walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker
        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.left_limit, self.right_limit = left_limit, right_limit
        super().__init__(start, home)

    def move(self):
        """Change position by +1 or -1 with equal probability."""
        position = self.position
        if position != self.left_limit and position != self.right_limit:
            super().move()


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """

        self.left_limit, self.right_limit = left_limit, right_limit
        super().__init__(start, home, seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        walker = Walker(self.start, self.home)
        position = walker.get_position()
        while position != self.left_limit and position != self.right_limit:
            return super().single_walk()


if __name__ == '__main__':
    num_walks = 20
    start_test = 0
    home_test = 20
    right_boundary_test = 20
    left_boundaries = [0, -10, -100, -1000, -10000]
    seed_test = 12345

    for left_end in left_boundaries:
        turn = BoundedSimulation(start_test, home_test, seed_test, left_end,
                                 right_boundary_test)
        durations = turn.single_walk()
        print(f'Left boundary = {left_end} gives: {durations}')
