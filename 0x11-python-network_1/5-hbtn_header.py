#!/usr/bin/python3
"""
takes in URL, sends request to URL & displays value of variable
X-Request-Id in the response header
"""

import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    header = r.headers.get("X-Request-Id")
    print(header)
