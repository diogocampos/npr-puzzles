#!/usr/bin/env python3

"""
NPR Sunday Puzzle, 29 July 2018

Find a common 2-word phrase with 4 letters in each word,
such that moving the 1st letter from the 2nd word to the end
results in an 8-letter word that sounds completely different.
"""

import util


def main():
    wordlist = list(util.all_wordlists())
    parts = set(filter(lambda w: len(w) is 4, wordlist))

    for word in filter(is_possible_solution, wordlist):
        solution = check_solution(word, parts)
        if solution: print(solution)


def is_possible_solution(word):
    return len(word) is 8 and word[0] is 'm'


def check_solution(word, parts):
    first = word[0:4]
    second = word[7] + word[4:7]
    if first in parts and second in parts:
        return f'{first} {second} -> {word}'


if __name__ == '__main__':
    main()


# Solution: mail slot -> maillots
