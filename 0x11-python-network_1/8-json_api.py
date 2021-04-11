#!/usr/bin/python3
# takes in letter & sends POST request to http://0.0.0.0:5000/search_user
# with letter as parameter

import requests
import sys


if __name__ == "__main__":
    if ((len(sys.agv)) < 2):
        q = ""
    else:
        q = sys.agv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        r = response.json()
        if r != {}:
            print("[{}] {}".format(r.get("id"), r.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
