#!/bin/bash
# makes request to 0.0.0.0:5000/catch_me causing server to respond with message 
curl -sL "X-HolbertonSchool-User-Id:98" PUT -H -d 0.0.0.0:5000/catch_me
