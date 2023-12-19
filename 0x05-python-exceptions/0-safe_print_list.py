#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        x = int(x)
    except ValueError as ValErrorr:
        print(valError)

    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count = count + 1
    except IndexError:
        pass
    finally:
        print()
        return count
