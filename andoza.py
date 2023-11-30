
import re
from uzwords import words
andoza = "^т...р$"

matches = []
for word in words:
    if re.match(andoza,word):
        matches.append(word)
print(matches)