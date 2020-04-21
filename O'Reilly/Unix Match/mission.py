import fnmatch
import re


def unix_match(filename: str, pattern: str) -> bool:
    regex = fnmatch.translate(pattern)
    return bool(re.match(regex, filename))

    # pattern = pattern.replace('.', '\.').replace('*', '.*') \
    #     .replace('?', '.').replace('[!', '[^').replace('[]', '[^.]') \
    #     .replace('[^]', '\[!\]')
    # print(f'pattern = {pattern}')
    # return bool(re.match(pattern, filename))
    # # your code here
    # return filename == pattern


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
