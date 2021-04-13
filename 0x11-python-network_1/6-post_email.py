#!/usr/bin/python3
"""
takes in URL & email address, sends POST request to passed URL
with email as parameter, & finally displays body of response
"""

import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
