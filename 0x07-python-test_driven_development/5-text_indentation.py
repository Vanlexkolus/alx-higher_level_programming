#!/usr/bin/python3
"""
This is a text indenting function
"""


def text_indentation(text):
    """
    This function takes in a long piece of text
    and indents it by dropping it 2 line down
    whenever it comes across any of the following 
    '.', '?'
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        r_strings = ["?", ".", ":"]
        index = 0
        while index < len(text):
            if index == 0:
                print(text[index], end="")
            else:
                if text[index - 1] in r_strings and text[index] == " ":
                    index += 1
                    continue
                else:
                    print(text[index], end="")
            for val in r_strings:
                if text[index] == val:
                    print()
                    print()
            if text[index] == " ":
                index += 1
            else:
                index += 1
