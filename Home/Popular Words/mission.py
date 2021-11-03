
def popular_words(text: str, words: list) -> dict:
    # your code here
    frequencies = {}
    for i in text.lower().split():
        count = frequencies.get(i ,0)

        if i in words:
            frequencies[i ] =coun t +1

    for i in words:
        if i not in text.lower().split():
            frequencies[i ] =0

    return frequencies


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
