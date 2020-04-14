from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    # your code here
    return sorted(items) == items and len(items) == len(set(items))


    # ascending = True
    # if len(items)==0:
    #     return True
    # previous_item = items.pop(0)
    # for item in items:
    #     if not item > previous_item:
    #         ascending = False
    #         break
    # return ascending

    # asc=sorted(items)
    # if len(items) == len(set(items)) and items==asc:
    #     return True
    # return False


if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
