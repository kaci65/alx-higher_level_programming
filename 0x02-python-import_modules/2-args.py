#!/usr/bin/python3
if __name__ == "__main__":
    import sys
args_list = len(sys.argv) - 1
if args_list == 0:
    print("{} arguments.".format(args_list))
elif args_list == 1:
    print("{} argument:".format(args_list))
else:
    print("{} arguments:".format(args_list))
    for index in range(args_list):
        index = index + 1
        print("{}: {}".format(index, sys.argv[index]))
