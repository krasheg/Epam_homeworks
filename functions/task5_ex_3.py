"""
Create function sum_geometric_elements, determining the sum of the first elements of a decreasing geometric progression
of real numbers with a given initial element of a progression `a` and a given progression step `t`, while the last
element must be greater than a given `lim`. `an` is calculated by the formula (an+1 = an * t), 0<t<1
Function must return float and round the answer to three decimal places using round().
Check the parameter `t` and raise a ValueError if it does not satisfy the inequality 0<t<1.
`a` and `lim` must be greater than 0, otherwise raise a ValueError.

Example,
For a progression, where a1 = 100, and t = 0.5, the sum of the first elements, greater than alim = 20, equals to
100+50+25 = 175
"""


def sum_geometric_elements(a1, t, lim):
    if t > 1 or t < 0 or a1 < 0 or lim < 0:
        raise ValueError
    result = []
    while a1 > lim:
        result.append(a1)
        a1 *= t
    return round(sum(result),3)



