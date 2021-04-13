#!/usr/bin/python3
"""
takes in letter & sends POST request to http://0.0.0.0:5000/search_user
with letter as parameter
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        response = r.json()
        if r:
            print("[{}] {}".format(response.get("id"), response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
