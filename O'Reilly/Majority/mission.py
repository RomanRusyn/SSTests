from collections import Counter


def is_majority(items: list) -> bool:
    # print(Counter(items))
    # if Counter(items)[True]>Counter(items)[False]:
    #     return True
    # else:
    #     return False

    # your code here
    return Counter(items)[True] > Counter(items)[False]


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
