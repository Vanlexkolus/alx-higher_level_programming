#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    for x in list(a_dictionary):
        if key == x:
            del a_dictionary[key]
    return a_dictionary
