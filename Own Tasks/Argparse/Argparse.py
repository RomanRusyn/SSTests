import argparse
import json
import os
import sys

my_parser = argparse.ArgumentParser(description='File parser. From path1 '
                                                'converts to path2')

my_parser.add_argument('-I',
                       action='store',
                       metavar='Path_input',
                       type=str,
                       help='the path to list input')

my_parser.add_argument('-o',
                       action='store',
                       metavar='Path_output',
                       type=str,
                       help='the path to list output')

my_parser.add_argument('-s',
                       action='store',
                       default=25,
                       type=int,
                       help='size of created dict in parsed file')

args = my_parser.parse_args()

input_path = args.I
output_path = args.o
count = args.s

if not os.path.isfile(input_path) or not os.path.isfile(output_path):
    print('The path specified does not exist')
    sys.exit()

print(f"input path->{input_path}, output path->{output_path}, count={count}")


# input_path = 'million.txt'
# output_path = 'out.txt'


def parser(path):
    general_list = []
    dict_25 = {}
    list_25 = []

    with open(path, 'r') as file:
        for line in file.readlines():
            dict_1 = {}
            sp_line = line.split('\t')
            dict_1["raw_url"] = sp_line[0]
            if len(list_25) < count:
                list_25.append(dict_1)
            else:
                dict_25["url"] = list_25
                list_25 = []
                general_list.append(dict_25)
                dict_25 = {}

    with open(output_path, 'w') as file:
        file.writelines(str(general_list).replace("'", "\""))
    return


parser(input_path)

with open(output_path, 'r') as handle:
    parsed = json.load(handle)
    print(json.dumps(parsed, indent=3, sort_keys=True))
