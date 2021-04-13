#!/usr/bin/python3
"""
takes in URL and email, sends POST request to passed URL with email as
parameter, & displays body of response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
        print(data)
