#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elems = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            elems = elems + 1
        except:
            pass
    print()
    return elems
