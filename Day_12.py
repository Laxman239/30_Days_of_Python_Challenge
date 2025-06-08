import re

with open("gmail_addresses.txt") as file:
    text = file.read()

pattern = r"^[a-zA-Z0-9._+]+@gmail\.com$"

matches = []
for line in text.splitlines():
    if re.match(pattern, line.strip()):
        matches.append(line.strip())

print(text)

print('Valid Gmail addresses:')
for match in matches:
    print(match)