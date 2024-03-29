"""
Write a function `fibonacci_loop(seq: list)`, which accepts a list of values and prints out values in one line on these
conditions:
 - floating point numbers should be ignored
 - string values should stop the iteration
 - loop control statements should be used

Example:
> fibonacci_loop([0, 1, 1.1, 1, 2, 99.9, 3, 0.0, 5, 8, "stop", 13, 21, 34])
0 1 1 2 3 5 8

"""


def fibonacci_loop(seq: list):
    result = []
    for num in seq:
        if isinstance(num, str):
            break
        elif isinstance(num, int):
            if not result:
                if num == 0:
                    result.append(num)
            elif len(result) == 1:
                if num == 1:
                    result.append(1)
            else:
                if num == result[-1] + result[-2]:
                    result.append(num)
    for i in result:
        print(i, end=" ")

