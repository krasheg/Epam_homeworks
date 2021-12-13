"""
Implement a function which takes a list of elements and returns a list of tuples containing pairs of this elements.
Pairs should be formed as in the example. If there is only one element in the list return `None` instead.
Using zip() is prohibited.

Examples:
> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]

> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

> get_pairs([1])
None

"""


def get_pairs(l: list) -> list[tuple]:
    result = []
    if len(l) ==1:
        return None
    else:
       for i in range(1,len(l)):
           result.append((l[i-1],l[i]))
    return result

print(get_pairs([1]))