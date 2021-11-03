def caps_lock(text: str) -> str:
    # your code here
    # return "".join(fragment.upper() if i%2 == 1 else fragment for i, fragment in enumerate(text.split('a')))
    a = text.split('a')
    print(a)
    for j in range(len(a)):
        print(j%2)
        if j % 2: a[j] = a[j].upper()
    return ''.join(a)


if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
