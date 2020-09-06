import random

def file_to_set_of_words(filename):
    """Converts a file with a word per line to a Python set"""

    words = []
    with open(filename, "r") as f:
        for line in f:
            words.append(line.strip())

    return set(words)
