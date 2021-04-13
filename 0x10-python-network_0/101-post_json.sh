#!/bin/bash
# sends JSON POST request to URL passed as 1st argument, displays body of response
curl -sL "$1" -X POST -H "Content-Type:application/json" -d @"$2"
