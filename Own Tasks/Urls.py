import re

from tld import *

"""Summary or Description of the Function

    Parameters:
    path (str): path to file with list of urls

    Returns:
    list: unique values from the file with urls

   """
path = 'domainNameFile.txt'


def uniqueUrls(path):
    rawUrls = []
    nonUniqueUrls = []
    with open(path, 'r') as file:
        for line in file.readlines():
            # print(get_fld(line, fix_protocol=True))
            rawUrls.append(line)
            nonUniqueUrls.append(get_fld(line, fix_protocol=True))

    urlDict = {}
    for n, r in zip(nonUniqueUrls, rawUrls):
        urlDict[n] = r
    # for key, values in urlDict.items():
    #     print(values, end='')
    return urlDict.values()


print(uniqueUrls(path))

# unike_url = []
#
# with open('C:/Users/rrusy/Desktop/domainNameFile.txt', 'r') as file:
#     for line in file.readlines():
#         pattern = re.findall('(http[s])*(\w*)(\.+)(\w*)(\.+)(\w*)', line)
#         for i in pattern:
#             if (''.join(i)) not in unike_url:
#                 unike_url.append(''.join(i))
#
# for i in unike_url:
#     print(i)
