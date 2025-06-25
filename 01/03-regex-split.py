import re

text = "zebra, lion, tiger, bear, elephant"
pattern = r',\s*'

# Using re.split() to split the text by the pattern
split_text = re.split(pattern, text)
if split_text:
    print("Split text: ", split_text)
else:
    print("No matches found to split.")