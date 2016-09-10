#!/usr/bin/env python

# NPR Sunday Puzzle, 3 Apr 2016

# Assuming each letter from 'a'..'z' corresponds to the numbers 1..26,
# find a 5-letter word where the 1st letter equals the "sum" of the other 4

# (takes a whitespace-delimited list of words as input from stdin)


import sys


def main():
    for line in sys.stdin:
        for word in line.split():
            if is_solution(word): print(word)


def is_solution(word):
    word = word.lower()
    return (
        len(word) == 5 and
        word.isalpha() and
        number(word[0]) == sum(number(c) for c in word[1:])
    )


def number(letter):
    return ord(letter) - ord('a') + 1


if __name__ == '__main__':
    main()


# Solutions: sadie, table, whack, zebra
