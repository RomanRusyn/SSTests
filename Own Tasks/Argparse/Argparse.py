path = 'million.txt'


def parser(path):
    general_list = []
    dict_25 = {}
    list_25 = []

    with open(path, 'r') as file:
        for line in file.readlines():
            dict_1 = {}
            sp_line = line.split('\t')
            dict_1["raw_url"] = sp_line[0]
            if len(list_25) <= 25:
                list_25.append(dict_1)
            else:
                dict_25["url"] = list_25
                list_25 = []
                general_list.append(dict_25)
                dict_25 = {}

    with open("out.txt", 'w') as file:
        file.writelines(str(general_list))


parser(path)
