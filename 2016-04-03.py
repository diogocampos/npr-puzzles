#!/usr/bin/env python3

"""
NPR Sunday Puzzle, 3 April 2016

Assuming each letter from 'a'..'z' corresponds to the numbers 1..26,
find a 5-letter word where the 1st letter equals the "sum" of the other 4.
"""

import util


def main():
    for word in util.all_wordlists():
        if is_solution(word): print(word)


def is_solution(word):
    return (len(word) is 5 and
        number(word[0]) == sum(number(c) for c in word[1:]))


def number(letter):
    return ord(letter) - ord('a') + 1


if __name__ == '__main__':
    main()


# Solutions: sadie, table, whack, zebra
