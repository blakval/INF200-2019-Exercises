def letter_freq(txt):
    t = txt.lower()
    txt = sorted(t)

    freq = {}

    for i in txt:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return freq


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))