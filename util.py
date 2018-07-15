import sys


def get_wordlist():
    if sys.stdin.isatty():
        print('Please pipe a wordlist into this script.', file=sys.stderr)
        return []
    return wordlist(sys.stdin)


def wordlist(file):
    for line in file:
        yield from (word for word in line.split() if word.isalpha())
