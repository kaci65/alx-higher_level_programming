#!/usr/bin/python3
# takes in URL, sends request to URL & displays value of variable
# X-Request-Id in the response header

import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    header = response.getheader("X-Request-Id")
    print(header)
