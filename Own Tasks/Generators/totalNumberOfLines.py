"""This file counts how much lines in the multiply files

"""

from findFiles import find_files
from printMore40Char import read_files


path = "TestFiles"
print(f'find_files->{find_files(path)}')

print(len(list(read_files(find_files(path)))))
