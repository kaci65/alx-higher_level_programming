#!/usr/bin/python3
for letters in range(97, 123):
     if chr(letters) not in "e" and chr(letters) not in "q":
        print("{}".format(chr(letters)), end= "")
