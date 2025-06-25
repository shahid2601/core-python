import re

text = "Before the rain, the sky was clear. After the rain, the sky was cloudy."
pattern = r'sky'
replacement = "atmosphere"

# Using re.sub() to replace all occurrences of the pattern in the text
new_text = re.sub(pattern, replacement, text)
if new_text:
    print("Modified text: ", new_text)
else:
    print("No matches found to replace.")