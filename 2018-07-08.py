#!/usr/bin/env python3

"""
NPR Sunday Puzzle, 8 July 2018

Find a US state whose name, after removing the last letter,
results in a series of state postal abbreviations.
Then find a major city in that state that also has this property.
"""

split = lambda words: [w.upper() for w in words.strip().split()]

NAMES = split('''
    Alabama Alaska Arizona Arkansas California Colorado Connecticut Delaware
    DistrictofColumbia Florida Georgia Hawaii Idaho Illinois Indiana Iowa
    Kansas Kentucky Louisiana Maine Maryland Massachusetts Michigan Minnesota
    Mississippi Missouri Montana Nebraska Nevada NewHampshire NewJersey
    NewMexico NewYork NorthCarolina NorthDakota Ohio Oklahoma Oregon
    Pennsylvania RhodeIsland SouthCarolina SouthDakota Tennessee Texas Utah
    Vermont Virginia Washington West Virginia Wisconsin Wyoming
    ''')

ABBRS = split('''
    AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS
    MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI
    WY
    ''')


def main():
    for name, abbrs in find_abbrs(NAMES):
        print('%s - %s' % (name, ','.join(abbrs)))


def find_abbrs(words):
    for word in words:
        letters = word[0:-1]
        pairs = [letters[i:i+2] for i in range(0, len(letters), 2)]
        if all(pair in ABBRS for pair in pairs):
            yield word, pairs


if __name__ == '__main__':
    main()


# Solutions:

# FLORIDA - FL,OR,ID    -> ORLANDO - OR,LA,ND
# MAINE - MA,IN
# NEWYORK - NE,WY,OR
