#!/bin/bash
# takes URL as argument, sends GET request to URL, displays body of the response
curl -sH X-HolbertonSchool-User-Id:98 "$1"
