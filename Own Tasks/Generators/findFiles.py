"""This file searches file path of all files in directory recursively

"""

import os

_path = "TestFiles"


def find_files(directory_path):
    """Finds file from """
    count_txt = 0
    file_name = []
    for dirpath, dirs, files in os.walk(directory_path):
        for f in files:
            file_name.append(os.path.join(dirpath, f))
            if f.split('.')[1] == 'txt':
                count_txt += 1
    return file_name


if __name__ == "__main__":
    print(find_files(_path))
