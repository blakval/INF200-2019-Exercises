from src.marie_kolvik_ex.ex01.letter_counts import letter_freq

def entropy(message):
    """
    Returns the entropy of a message calculated with this formula:
    H = - \sum_i p_i \log_2 p_i
    Where:
    N : Number of letters i message
    n_i : number of occurences of letter i
    p_i = n_i/N : frequency of the letter in the message
    """


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))