#!/usr/bin/python3
"""
takes in URL, sends request to URL & displays body of response (decoded
in utf-8)
manage urllib.error.HTTPError exceptions and print: Error code
followed by the HTTP status code
"""

import urllib.request
import urllib.parse
import urllib.error
from sys import argv


if __name__ == "__main__":
    req = argv[1]
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            print(data)
    except:
        urllib.error.URLError as e:
            print("Error code: {}".format(e.code))
