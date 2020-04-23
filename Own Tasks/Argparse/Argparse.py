"""Script for parsing url file

The Example of usage:
    python Argparse.py -I 'million.txt' -o 'out.txt' -s 25

    usage: Argparse.py [-h] [-I Path_input] [-o Path_output] [-s BATCHSIZE]
    optional arguments:
          -h, --help            show this help message and exit
          -I Path_input, --input Path_input
                                the path to list input
          -o Path_output, --output Path_output
                                the path to list output
          -s BATCHSIZE, --batchsize BATCHSIZE
                                size of created dict in parsed file

"""

import argparse
import json
import os
import sys


def main():
    """Main function for launching argparser and file parser in a bunch"""
    my_parser = argparse.ArgumentParser(description='File parser. From path1 '
                                                    'converts to path2')

    my_parser.add_argument('-I',
                           '--input',
                           action='store',
                           metavar='Path_input',
                           type=str,
                           help='the path to list input')

    my_parser.add_argument('-o',
                           '--output',
                           action='store',
                           metavar='Path_output',
                           type=str,
                           help='the path to list output')

    my_parser.add_argument('-s',
                           '--batchsize',
                           action='store',
                           default=25,
                           type=int,
                           help='size of created dict in parsed file')

    args = my_parser.parse_args()

    input_path = args.input
    output_path = args.output
    size_dictionary = args.batchsize

    if not os.path.isfile(input_path) or not os.path.isfile(output_path):
        print('The path specified does not exist')
        sys.exit()

    print(
        f"input path-{input_path}, output path-{output_path}, count={size_dictionary}")

    def parser(path, dict_size):
        """File parser

        This function takes path to file for parsing, size of dictionary output
        size.

        Reads file line by line, choosing url address and replaces it into the
        output file in JSON format:
        [
            {"url": [
                {"raw_url": "google.com"},
                {"raw_url": "microsoft.com"},
                {"raw_url": “yahoo.co.ip"},
                ....
                ]}
        ]

        """
        general_list = []
        formation_dictionary_25items = {}
        list_with_25elements = []

        with open(path, 'r') as file:
            for line in file.readlines():
                dict_with_1item = {}
                sp_line = line.split('\t')
                dict_with_1item["raw_url"] = sp_line[0]
                if len(list_with_25elements) < dict_size:
                    list_with_25elements.append(dict_with_1item)
                else:
                    formation_dictionary_25items["url"] = list_with_25elements
                    list_with_25elements = []
                    general_list.append(formation_dictionary_25items)
                    formation_dictionary_25items = {}

        with open(output_path, 'w') as file:
            file.writelines(str(general_list).replace("'", "\""))

    parser(input_path, size_dictionary)

    with open(output_path, 'r') as handle:
        parsed = json.load(handle)
        print(json.dumps(parsed, indent=3, sort_keys=True))


if __name__ == "__main__":
    sys.exit(main())
