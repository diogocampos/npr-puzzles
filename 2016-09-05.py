#!/usr/bin/env python3

"""
NPR Sunday Puzzle, 5 September 2016

Find a 5-letter word containing 'rn' such that
changing 'rn' to 'm' results in its opposite.
"""

import util


def main():
    wordlist = list(util.get_wordlist())
    if not wordlist: return 1

    for word in wordlist:
        if is_possible_solution(word, wordlist):
            print(word, counterpart(word))


def is_possible_solution(word, wordlist):
    word = word.lower()
    return (
        len(word) == 5 and
        'rn' in word and
        counterpart(word) in wordlist
        )


def counterpart(word):
    return word.replace('rn', 'm')


if __name__ == '__main__':
    import sys
    sys.exit(main())


# Solution: 'stern' and 'stem'
