import re


match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
print(match.group(1))