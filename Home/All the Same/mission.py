from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    # if len(elements)==0:
    #     return True
    # n = elements[0]
    # coont=0
    # for i in elements:
    #     if i==n:
    #         coont+=1
    #
    # if len(elements)==coont:
    #     return True
    # else:
    #     return False
    x = all(el == elements[0] for el in elements)
    print(x)
    return x


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 2, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
