import re


# Compile the pattern to improve performance
# Inspired by: https://stackoverflow.com/a/1176023/13089670
pattern = re.compile(r'(?<!^)(?=[A-Z])')


def pascal_to_snake_case(text):
    text = text.strip()
    return pattern.sub('_', text).lower()
