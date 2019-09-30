from src.marie_kolvik_ex.ex01.letter_counts import letter_freq


def entropy(message):
    """
    Returns the entropy of a message calculated with this formula:
    H = - sum( p_i * log_2(p_i))
    Where
    N: Number of letters in message, variablename tot_letters
    n_i : number of occurences of letter i
    p_i = n_i/N : frequency of the letter in the message

    Input:
    -----
    Message to test.

    Output:
    -------
    Entropy
    """
    from math import log2

    tot_letters = len(message)

    h = []
    counts = letter_freq(message)
    for letter, count in counts.items():
        p_i = count / tot_letters
        h.append(-p_i * log2(p_i))

    entropy_sum = sum(h)

    return entropy_sum


if __name__ == "__main__":
    for msg in "", "aaaa", "aaba", "abcd", "This is a short text.":
        print("{:25}: {:8.3f} bits".format(msg, entropy(msg)))
