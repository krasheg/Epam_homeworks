"""
Write a function that checks whether a string is a palindrome or not.
Return 'True' if it is a palindrome, else 'False'.

Note:
Usage of reversing functions is required.
Raise ValueError in case of wrong data type

To check your implementation you can use strings from here
(Palindrome#Famous_palindromes).
"""


def is_palindrome(string):
    if not isinstance(string, str):
        raise ValueError
    return string.lower() == "".join(list(reversed(string.lower())))




