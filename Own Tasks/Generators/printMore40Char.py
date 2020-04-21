"""This file reads file path and prints everything from file in length of
line is more than n

"""


def read_files(filenames):
    """Reads file line by line"""
    for file in filenames:
        for line in open(file, 'r'):
            yield line
        print()


def grep(pattern, lines):
    """Greps pattern from line in file"""
    return (line for line in lines if len(line) > pattern)


def print_lines(lines):
    """Prints lines from file"""
    for line in lines:
        print(line, end="")


def main(pattern, filenames):
    """Combines functions print_lines, grep, read_files for easier usage"""
    lines = read_files(filenames)
    lines = grep(pattern, lines)
    print_lines(lines)


if __name__ == "__main__":
    main(15, ("TestFiles\\someStrings.txt",
              "TestFiles\\domainNameFile.txt"))
