from itertools import combinations

BRACKETS = {
    '(' : ')',
    '[' : ']',
    '{' : '}'
}

def is_balanced(s):
    stack = ['']
    for ch in s:
        if ch in BRACKETS:
            stack.append(BRACKETS[ch])
        elif ch in BRACKETS.values() and ch != stack.pop():
            return False
    return stack == ['']

def remove_brackets(a):
    for length in reversed(range(len(a) + 1)):
        for combination in reversed(tuple(combinations(a, length))):
            if is_balanced(combination):
                return ''.join(combination)

if __name__ == '__main__':
    print("Example:")
    print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")
