from src.marie_kolvik_ex.ex01.letter_counts import letter_freq


def char_counts(textfilename):
    """
    Opens the file using encoding utf-8 and reads the entire file
    content into a single string. Then counts how often each character code
    (0 - 255) occurs in the string and return the result as a list or tuple
    where result[i] gives the number of occurances of character code i.
    """
    file = open(textfilename)
    string = file.read()
    file.close()

    counts = letter_freq(string)

    return counts


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
