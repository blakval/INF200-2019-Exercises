# -*- coding: utf-8 -*-

__author__ = 'Marie Kolvik Valøy'
__email__ = 'mvaloy@nmbu.no'


class BoundedWalker:
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


class BoundedSimulation:
    pass
