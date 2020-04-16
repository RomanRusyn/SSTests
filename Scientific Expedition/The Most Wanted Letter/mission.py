from collections import Counter


def checkio(text: str) -> str:
    # replace this for solution
    # return (lambda x: max(x, key=x.count))(sorted([i for i in text.lower() if i.isalpha()]))
    counts = sorted(ch.lower() for ch in text if ch.isalpha())
    print(Counter(counts).most_common(1))
    return Counter(counts).most_common(1)[0][0]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")