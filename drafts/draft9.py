# Regular expressions
import re

# Search for pattern
match = re.search(r"\d+", "Order 1234")
print(match.group())  # Output: 1234

# Find all matches
numbers = re.findall(r"\d+", "There are 3 cats and 4 dogs")
print(numbers)  # Output: ['3', '4']

# Replace text
text = re.sub(r"\d+", "X", "Room 101")
print(text)  # Output: Room X

import re

# Search for a pattern
match = re.search(r"\d+", "Room 101 d 2") # Finds the first sequence of digits
print(match.group())

# Find all matches
numbers = re.findall(r"\d+", "There are 32 cats and 4 dogs")
print(numbers)

# r"\D" means anything that ISN'T numbers
# r"\w" is any word

match = re.search(r'\d', val, re.ASCII)
print(match.group())

# The difference between \d and \d+ is

# Regex: r'colou?r'
# r"-.*-"
# r'ax*a' -> aa, axa, axxxxa. any nuber of the character bellow can appear/
# r'ax+a' -> like * but without accepting aa.
# r'ax?a' -> aa, axa
# r'ax{2,4}a' (or {3,} or {17}) -> specific number of times!

# it can match to a part of the word as well.
# + is any number of characters that i'd wish (except 0)


# Greedy quantifiers
# If you put a*, and there is no a in the beginning, it would return an empty string.
# r'^cat' -> will only much in the beginning
# what do you do if you want to do regular expressions with saved characters?
# <[^>]*>