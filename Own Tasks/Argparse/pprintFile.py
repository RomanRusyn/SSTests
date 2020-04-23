# import json
#
# with open('out.txt', 'r') as handle:
#     parsed = json.load(handle)
#     print(json.dumps(parsed, indent=3, sort_keys=True))
# # with open("out.txt","r") as file:
# #     pprint(file.read(800),width=40,depth=1001)
# # pprint(outfile, indent=2, width=80, depth=10,  compact=False,
# #        sort_dicts=True)
#
# # pprint(outfile, indent=2, width=80, depth=10,  compact=False, sort_dicts=True)
#
# import argparse
#
# import os
# import sys
#
# # Create the parser
# my_parser = argparse.ArgumentParser(description='File parser. From path1 '
#                                                 'converts to path2')
#
# my_parser.add_argument('-I',
#                        action='store',
#                        metavar='Path_input',
#                        type=str,
#                        help='the path to list input')
#
# my_parser.add_argument('-o',
#                        action='store',
#                        metavar='Path_output',
#                        # default='out.txt',
#                        type=str,
#                        help='the path to list output')
#
# my_parser.add_argument('-s',
#                        action='store',
#                        default=25,
#                        type=int,
#                        help='size of created dict in parsed file')
#
# args = my_parser.parse_args()
#
# input_path = args.I
# output_path = args.o
# count = args.s
#
# if not os.path.isfile(input_path) or not os.path.isfile(output_path):
#     print('The path specified does not exist')
#     sys.exit()
#
# print(f"input path->{input_path}, output path->{output_path}, count={count}")
