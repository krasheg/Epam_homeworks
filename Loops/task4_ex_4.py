"""
Implement a function `split_by_index(string: str, indexes: List[int]) -> List[str]` which splits the `string` by indexes specified in `indexes`.
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.

Examples:
python
split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

split_by_index("no luck", [42])
["no luck"]

"""


def split_by_index(string: str, indexes: list[int]) -> list[str]:
    newlist = []
    result = []
    start = 0
    for index, item in enumerate(indexes):
        if isinstance(item, int) and item >= 0:
            if newlist and item <= newlist[-1]:
                continue
            newlist.append(item)
    for index, num in enumerate(newlist):
        if index == 0:
            result.append(string[:num])
            start = num
        elif num > newlist[index - 1]:
            result.append(string[start:num])
            start = num
            if index == len(newlist) - 1:
                result.append(string[num:])
        continue
    return result



