import re


def unix_match(filename: str, pattern: str) -> bool:

    # your code here
    pattern = pattern.replace('.', '\.').replace('*', '.*').replace('?', '.').replace('[!','[^').replace('[]','[^.]').replace('[^]', '\[!\]')
    print(f'pattern = {pattern}')
    m = re.match("name.txt", "name.txt").group()
    print(f'm={m}')
    return bool(re.match(pattern, filename))


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
