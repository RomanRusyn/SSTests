import re


def is_stressful(subj):
    """
        recognize stressful subject
    """
    list_words = ["help", "asap", "urgent"]
    list_subj = subj.split(" ")
    for i in list_subj:
        if i.casefold() in list_words:
            return True
    if subj.endswith("!!!") or subj.isupper():
        return True
    for k in subj.lower().split():
        for h in list_words:
            if re.search('+[^0-9a-z]*'.join(h), k):
                return True
    return False


if __name__ == '__main__':
    # These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
