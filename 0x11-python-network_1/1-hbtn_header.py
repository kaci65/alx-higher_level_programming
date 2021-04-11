#!/usr/bin/python3
# takes in URL, sends request to URL & displays value of X-Request-Id
# variable found in header of response

import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.getheader("X-Request-Id")
        print(header)
