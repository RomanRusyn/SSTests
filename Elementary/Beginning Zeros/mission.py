def beginning_zeros(number: str) -> int:
    # your code here
    if number.startswith('0000'):
        return 4
    elif number.startswith('000'):
        return 3
    elif number.startswith('00'):
        return 2
    elif number.startswith('0'):
        return 1
    else:
        return 0


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")
