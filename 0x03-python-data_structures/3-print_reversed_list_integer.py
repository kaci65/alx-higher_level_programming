#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_my_list = my_list[::-1]
    for item in range(len(new_my_list)):
        print('{}'.format(new_my_list[item]))
