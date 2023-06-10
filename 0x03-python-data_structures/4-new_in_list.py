#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    i = 0
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        while i <= len(my_list) - 1:
            if i != idx:
                new_list.append(my_list[i])
            if i == idx:
                new_list.append(element)
            i += 1
        return new_list
