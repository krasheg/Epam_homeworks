"""
Implement function count_letters, which takes string as an argument and returns a dictionary that contains letters of
given string as keys and a number of their occurrence as values.

Example:
print(count_letters("Hello world!"))
Result: {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

Note: Pay attention to punctuation.
"""


def count_letters(s):
    if not isinstance(s, str):
        raise TypeError
    s = "".join([i for i in s if i.isalpha()])
    result = {}
    for let in s:
        result[let] = result.get(let, 0) + 1
    return result
