#!/bin/bash
# sends request to URL passed as argument, displays only status code of response
curl -soI "$1" /dev/null --write-out "%{http_code}"
