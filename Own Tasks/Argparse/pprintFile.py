from Argparse import parser, write_to_file

write_to_file(parser("ten.txt", 3), "new_test.txt")
dd = parser("ten.txt", 3)
print(dd)

# with open("new_test.txt", 'r') as file:
#     print(file.read())
