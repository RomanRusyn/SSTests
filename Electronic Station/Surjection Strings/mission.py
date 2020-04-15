def isometric_strings(str1: str, str2: str) -> bool:
    # your code here
    print(len(set(zip(str1,str2))),len(set(str1)))
    # a = sorted(zip(str1,str2))
    # print(a)
    return len(set(str1)) == len(set(zip(str1, str2)))


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
