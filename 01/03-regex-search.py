import re

text = "The rain in spain stays mainly in the plain."
pattern = r' in '

# Using re.search() to find the first occurrence of the pattern in the text
match = re.search(pattern, text)
if match:
    print("Match found at position: ", match.start())
    print("Matched text: ", match.group())
else:
    print("No match found.")