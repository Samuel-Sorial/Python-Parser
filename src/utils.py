import re

pattern = re.compile(r'(?<!^)(?=[A-Z])')


def pascal_to_snake_case(text):
    text = text.strip()
    return pattern.sub('_', text).lower()
