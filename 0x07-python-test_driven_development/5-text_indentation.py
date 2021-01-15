#!/usr/bin/python3
"""Printing strings"""


def text_indentation(text):
    """function to print text with 2 new lines after (., ? and :)"""
    if not isinstance(text, (str)):
        raise TypeError("text must be a string")
    else:
        character = ['?', ':', '.']
        sliced_str = ""
        for line in text:
            sliced_str += line
            if line in character:
                sliced_str += "\n"
                print(sliced_str.strip(" "))
                sliced_str = ""
    if line not in character:
        print(sliced_str.strip(" "), end="")

