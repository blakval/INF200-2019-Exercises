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


class ListRand:
    def __init__(self, list_of_seeds):
        self.r = list_of_seeds
        self.n = - 1

    def rand(self):
        self.n += 1
        if self.n == len(self.r):
            raise RuntimeError('No more numbers')
        else:
            return self.r[self.n]


if __name__ == '__main__':
    r = LCGRand(5)
    r1 = r.rand()
    r12 = r.rand()
    r = LCGRand(103)
    r2 = r.rand()
    print(f'When using LCGRand: Seed five gives {r1} first time, {r12} '
          f'second time. Seed 103 gives {r2}.')

    test_liste = [8, 10, 4, 8]
    ra = ListRand(test_liste)
    ra1 = ra.rand()
    ra2 = ra.rand()
    print(f'When using ListRand: The two first numbers are {ra1} and {ra2}')
