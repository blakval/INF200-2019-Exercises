# -*- coding: utf-8 -*-

__author__ = 'Marie Kolvik Valøy'
__email__ = 'mvaloy@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.r = seed

    def rand(self):
        a = 7 ** 5
        m = 2 ** 31 - 1
        self.r = (a * self.r % m)
        return self.r
