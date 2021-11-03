def goes_after(word: str, first: str, second: str) -> bool:
    # your code here
    return word.find(second)>word.find(first)>-1
    # return True if word.find(first) > -1 and word.find(second)>word.find(first) else False


if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
