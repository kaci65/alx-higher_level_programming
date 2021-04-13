#!/usr/bin/python3
"""
takes in URL, sends request to URL and displays body of the response
If HTTP status code is >= 400, print: Error code: followed by value
of HTTP status code
"""

import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if response.raise_for_status >= 400:
        print("Error code: {}".format(response.raise_for_status))
    else:
        print(response.text)
