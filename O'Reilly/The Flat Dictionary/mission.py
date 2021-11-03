def flatten(dictionary):
    # your code here
    result_dict = {}

    def unpack(inner_dict, s=''):
        for key in inner_dict:
            if type(inner_dict[key]) != dict:
                result_dict[s + key] = inner_dict[key]
            elif inner_dict[key] == {}:
                result_dict[s + key] = ''
            else:
                unpack(inner_dict[key], s + key + '/')

    unpack(dictionary)
    return result_dict

    # if all(type(v) is str for v in dictionary.values()):
    #     return dictionary
    # resuly_dict = {}
    # for key in dictionary.keys():
    #     if type(dictionary[key]) == str:
    #         resuly_dict[key] = dictionary[key]
    #     elif len(dictionary[key]) == 0:
    #         resuly_dict[key] = ''
    #     else:
    #         flat_key = flatten(dictionary[key])
    #         print(f'flat_key->{flat_key}')
    #         for eKey in flat_key:
    #             print(f'eKey->{eKey}')
    #             resuly_dict[key + '/' + eKey] = flat_key[eKey]
    # return resuly_dict


if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
