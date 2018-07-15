#!/usr/bin/env python

# NPR Sunday Puzzle, 31 January 2016

# Find two pairs of (country, city) in the Middle East,
# such that both pairs contain the same 12 letters


COUNTRIES = [
    'arabia', 'bahrain', 'cyprus', 'egypt', 'emirates', 'iran', 'iraq',
    'israel', 'jordan', 'kuwait', 'lebanon', 'oman', 'palestine', 'qatar',
    'syria', 'turkey', 'yemen',
    ]

CITIES = [
    'abudhabi', 'acre', 'adana', 'aden', 'aleppo', 'alexandria', 'amman',
    'ankara', 'aqaba', 'ashur', 'aswan', 'asyut', 'baghdad', 'beirut', 'bursa',
    'bushehr', 'byblos', 'cairo', 'damascus', 'doha', 'dubai', 'fallujah',
    'gaza', 'giza', 'istanbul', 'izmir', 'jeddah', 'jerash', 'jericho',
    'jerusalem', 'luxor', 'manama', 'mecca', 'medina', 'mosul', 'muharraq',
    'muscat', 'nicosia', 'petra', 'rafah', 'ramallah', 'riyadh', 'sanaa',
    'tehran', 'telaviv', 'tikrit', 'suez',
    ]


def main():
    pairs = []

    for country in COUNTRIES:
        for city in CITIES:
            if len(country) + len(city) == 12:
                pairs.append(country + ' ' + city)

    for i, pair1 in enumerate(pairs):
        for pair2 in pairs[i+1:]:
            if letters(pair1) == letters(pair2):
                print(pair1 + ' / ' + pair2)


def letters(string):
    return ''.join(sorted(string))


if __name__ == '__main__':
    main()


# Solution: (Bahrain, Dubai) and (Iran, Abu Dhabi)
