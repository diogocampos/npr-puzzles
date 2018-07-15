#!/usr/bin/env coffee

# NPR Sunday Puzzle, 31 January 2016

# Find two pairs of (country, city) in the Middle East,
# such that both pairs contain the same 12 letters


COUNTRIES = [
  'arabia', 'bahrain', 'cyprus', 'egypt', 'emirates', 'iran', 'iraq', 'israel',
  'jordan', 'kuwait', 'lebanon', 'oman', 'palestine', 'qatar', 'syria',
  'turkey', 'yemen',
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


main = ->
  pairs = []

  for country in COUNTRIES
    for city in CITIES
      if country.length + city.length is 12
        pairs.push "#{country} #{city}"

  for pair1, index in pairs
    for pair2 in pairs.slice (index + 1)
      if letters(pair1) is letters(pair2)
        console.log pair1, '/', pair2


letters = (string) ->
  ltrs = string.split('')
  ltrs.sort()
  ltrs.join('')


if module is require.main
  main()


# Solution: (Bahrain, Dubai) and (Iran, Abu Dhabi)
