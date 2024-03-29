from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    # your code here
    # print(items.index(border)+1)
    if len(items) == 0 or border not in items:
        print(items)
        return items

    return items[:items.index(border) + 1]


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_after([1, 1, 5, 6, 7], 2)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
    assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_after([], 0)) == []
    assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
