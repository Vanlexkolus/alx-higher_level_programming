#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    #created a copy of the main list

    new = list(my_list)
    
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        new[idx] = element
        return new
