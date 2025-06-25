import re

text = "The weather in New York is sunny and warm."
pattern = r'New York'

# Using re.search() to find the pattern in the text
match = re.search(pattern, text)
if match:
    print("Match found: ", match.group())
else:
    print("No match found.")