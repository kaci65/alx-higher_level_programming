#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    for i in new_string:
        if i in 'Cc':
            del(new_string[new_string.index(i)])
            return ''.join(new_string)
