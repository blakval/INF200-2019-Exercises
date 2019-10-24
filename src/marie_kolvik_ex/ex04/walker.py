# -*- coding: utf-8 -*-

__author__ = 'Marie Kolvik Valøy'
__email__ = 'mvaloy@nmbu.no'

from random import randint


class Walker:
    def __init__(self, start, home):
        self.position = start
        self.home = home
        self.number_of_steps = 0

    def move(self):
        step = randint(0, 1)
        self.number_of_steps += 1
        if step == 0:
            step = -1
        if self.position == self.home:
            return'The student is at home'
        else:
            self.position += step

    def is_at_home(self):
        if self.position == self.home:
            return'The student is at home'
        else:
            return'The student is not at home'

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.number_of_steps
