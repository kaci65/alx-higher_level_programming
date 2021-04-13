#!/bin/bash
# sends request to URL passed as argument, displays only status code of response
curl -o /dev/null -s -w "%{http_code}" "$1"
