#!/usr/bin/python3
# a function that finds the biggest integer of a list
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        High_num = my_list[0]
        for i in my_list:
            if i > High_num:
                High_num = i
        return High_num
