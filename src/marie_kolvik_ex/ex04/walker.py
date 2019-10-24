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
            self.position -= 1
        else:
            self.position += 1

    def is_at_home(self):
        return self.position == self.home

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.number_of_steps


if __name__ == '__main__':
    start_position = 0
    homes = [1, 2, 5, 10, 20, 50, 100]
    number_of_times = 5

    def wandering(starr, homm):
        walker = Walker(starr, homm)
        while walker.get_position() != homm:
            walker.move()
        return walker.get_steps()

    for i in homes:
        lengths = []
        for j in range(number_of_times):
            lengths.append(wandering(start_position, i))

        print(f'Distance: {i} -> Path lengths:{lengths}')
