import re


def find_quotes(a):
    # your code here
    # s = a[a.find("(")+1:a.find(")+")]
    # s = str(re.findall('\".*\"',a)).replace("\"","").replace("'","").replace("[","").replace("]","")
    # l=a.split("\"")
    # empty=[]
    # ne=[]
    # l.append(s)
    # print(l)
    # for i in l:
    #     if len(i):
    #         ne.append(i)
    # print(ne)
    # for i in ne:
    #     if len(i)
    # search_results = re.finditer(r'\".*?\"', a)
    # result = re.search(r'"(.*?)"', a)
    # print(result)
    # print(result.group(1))
    # return result.group(1) if "\"" in a else empty

    # return  result
    #     # return re.findall(r'"(.*?)"', a)
    #     # quotes = []
    #     # words = []
    #     #
    #     # nxt = a.find('"')
    #     # while nxt > -1:
    #     #     quotes.append(nxt)
    #     #     nxt = a.find('"', nxt + 1)
    #     #
    #     # for i in range(0, len(quotes) - 1, 2):
    #     #     left, right = quotes[i], quotes[i + 1]
    #     #     words.append(a[left + 1:right])
    #     #
    #     # return words

    # results = []
    # quoted_str =""
    # quoted =  False
    #
    # for c in a:
    #     if c == '"':
    #         if quoted: # end quote
    #             results.append(quoted_str)
    #             quoted_str =""
    #             quoted =  False
    #         else:      # start quote
    #             quoted = True
    #     elif quoted:
    #         quoted_str += c
    #
    # return results

    result_list = []
    result_word = ""
    trigger = 0
    for symbol in a:
        if symbol == '"' and trigger == 0:
            trigger = 1
            continue
        if symbol == '"' and trigger == 1:
            trigger = 0
            result_list.append(result_word)
            result_word = ""
        if trigger == 1:
            result_word += symbol

    return result_list


if __name__ == '__main__':
    print("Example:")
    print(find_quotes('"Greetings"'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_quotes('"Greetings"') == ['Greetings']
    assert find_quotes('Hi') == []
    assert find_quotes('good morning mister "superman"') == ['superman']
    assert find_quotes('"this" doesn\'t make any "sense"') == ['this', 'sense']
    assert find_quotes('"Lorem Ipsum" is simply dummy text '
                       'of the printing and typesetting '
                       'industry. Lorem Ipsum has been the '
                       '"industry\'s standard dummy text '
                       'ever since the 1500s", when an '
                       'unknown printer took a galley of '
                       'type and scrambled it to make a type '
                       'specimen book. It has survived not '
                       'only five centuries, but also the '
                       'leap into electronic typesetting, '
                       'remaining essentially unchanged. "It '
                       'was popularised in the 1960s" with '
                       'the release of Letraset sheets '
                       'containing Lorem Ipsum passages, and '
                       'more recently with desktop '
                       'publishing software like Aldus '
                       'PageMaker including versions of '
                       'Lorem Ipsum.') == ['Lorem Ipsum',
                                           "industry's standard dummy text ever "
                                           'since the 1500s',
                                           'It was popularised in the 1960s']
    assert find_quotes('count empty quotes ""') == ['']
    print("Coding complete? Click 'Check' to earn cool rewards!")
