def checkio(first, second):
    f=first.split(',')
    s=second.split(',')
    lis=[]
    for i in range(len(f)):
        if f[i] in s:
            lis.append(f[i])
    print(str(lis))

    st=','.join(sorted(lis))
    print(st)
    # for k in lis:
    #     print(f'k={k}')
    #     st+=''.join(k)
    # print(st)
    return st


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
