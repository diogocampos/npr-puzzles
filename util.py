from pathlib import Path

WORDLISTS_DIR = Path(__file__).parent / 'wordlists'


def wordlist(filename):
    return read_words(WORDLISTS_DIR / filename)


def all_wordlists():
    for path in WORDLISTS_DIR.glob('*.txt'):
        yield from read_words(path)


def read_words(path):
    with open(path, 'r') as file:
        for line in file:
            for word in line.split(): yield word.lower()
