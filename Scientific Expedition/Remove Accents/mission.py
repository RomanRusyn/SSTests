from unicodedata import normalize, category


def checkio(in_string):
    "remove accents"
    # print(''.join(c for c in normalize('NFC', in_string) if category(c) !='Mn'))
    # print(normalize('NFD',in_string))
    # print(category(in_string[5]))
    for i in in_string:
        print(normalize('NFC',i) if category(i)!='Mn' else None)
    print("---")
    return ''.join(c for c in normalize('NFD', in_string) if category(c) != 'Mn')
    # These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
