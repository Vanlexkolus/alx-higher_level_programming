#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        #list indices start from 0, so the valid indices are 0, 1, 2, ..., len(my_list)-1. If idx is equal to the length of the list, it will be out of range.
        return None
    else:
        return my_list[idx]
