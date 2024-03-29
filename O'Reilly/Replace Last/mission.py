from typing import Iterable


def replace_last(items: list) -> Iterable:
    # your code here
    def create_multipliers():
        return [lambda x: i * x for i in range(5)]

    for multiplier in create_multipliers():
        print(multiplier(2))
    print(items[-1:])
    print(items[:-1])
    return items[-1:] + items[:-1]


if __name__ == '__main__':
    print("Example:")
    print(list(replace_last([2, 3, 4, 1])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
    assert list(replace_last([1])) == [1]
    assert list(replace_last([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
