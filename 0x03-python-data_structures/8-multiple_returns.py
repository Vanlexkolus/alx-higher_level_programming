#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    else:
        length = len(sentence)
        char = sentence[0]
        return (length, char)
