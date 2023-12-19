#!/usr/bin/python3
def raise_exception():
    try:

        strAndInt = 1 + 'boy'
        return strAndInt

    except TypeError:
        raise
