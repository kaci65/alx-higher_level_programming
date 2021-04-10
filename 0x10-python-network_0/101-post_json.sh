#!/bin/bash
# sends JSON POST request to URL passed as 1st argument, displays body of response
curl -s -L "$1" -X POST -H -d "Content-Type:application/json" @"$2"
