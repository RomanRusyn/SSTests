def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """

    # if text.endswith('.'):
    #     print(f'if statment {text.capitalize()}')
    #     return text.capitalize()
    # else:
    #     print(f'else statment raw->{text} modified-> {text.capitalize()+"."}')
    #     return text.capitalize() + '.'

    # your code here
    # text = text[0].upper() + text[1:]
    # if text.endswith('.'):
    #     return text
    # else:
    #     return text +'.'

    # print(text.capitalize() + '.' if not (text.endswith('.')) else '')
    # return text.capitalize() + '.' if not text.endswith('.') else ''
    # return text.capitalize() if text.endswith('.') else text.capitalize()+'.'
    return text if text.endswith('.') else text[0].upper() + text[1:] + '.'


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
