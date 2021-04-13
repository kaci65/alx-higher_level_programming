#!/bin/bash
# sends request to URL passed as argument, displays only status code of response
curl -s -o -I /dev/null "$1" --write-out "%{http_code}"
