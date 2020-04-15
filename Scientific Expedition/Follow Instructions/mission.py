from collections import Counter


def follow(instructions):
    # your code here
    c = Counter(instructions)
    return (c['r'] - c['l'], c['f'] - c['b'])
    # fb=0
    # lr=0
    # for i in instructions:
    #     if i=='f':
    #         fb+=1
    #     elif i=='b':
    #         fb-=1
    #     elif i=='l':
    #         lr-=1
    #     elif i=='r':
    #         lr+=1
    # return (lr, fb)



if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
