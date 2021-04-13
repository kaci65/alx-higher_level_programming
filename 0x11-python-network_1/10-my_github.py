#!/usr/bin/python3
"""
takes your Github credentials (username & password) & uses Github API
to display your id
"""

from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get('https://api.github.com/user', auth=('username',
                                                          'password'))
    r = r.json
    print(r.get("id"))
