import re

text = "The mountain is high, and the river is deep. The mountain is also beautiful."
pattern = r'mountain'

# Using re.findall() to find all occurrences of the pattern in the text
matches = re.findall(pattern, text)
if matches:
    print("Matches found: ", matches)
else:
    print("No matches found.")