def squares_by_loop(n):
    liste = []
    for k in range(n):
        if k % 3 == 1:
            liste.append(k ** 2)

    return liste


def squares_by_comp(n):
    return [k ** 2 for k in range(n) if k % 3 == 1]


if __name__ == '__main__':
    if squares_by_loop(n=10) != squares_by_comp(n=10):
        print('ERROR!')
