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

    response = requests.get('https://api.github.com/user', auth=(username,
                                                                 password))
    try:
        response = r.json()
        print(response.get("id"))
    except ValueError:
        print("Not a valid JSON")
