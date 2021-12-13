"""
Implement `swap_quotes` function which receives a string and replaces all " symbols with ' and vise versa.
The function should return modified string.

Note:
Usage of built-in or string replacing functions is required.
"""


def swap_quotes(string):
    return string.translate(string.maketrans('"\'', '\'"'))
