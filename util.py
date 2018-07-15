from pathlib import Path


def all_wordlists():
    dir = Path(__file__).parent / 'wordlists'
    for filename in dir.glob('*.txt'):
        with open(filename, 'r') as file:
            yield from wordlist(file)


def wordlist(file):
    for line in file:
        for word in line.split():
            if word.isalpha(): yield word.lower()
