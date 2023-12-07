#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    Dic_2 = {}
    for a, b in a_dictionary.items():
        Dic_2[a] = b * 2
    return Dic_2
