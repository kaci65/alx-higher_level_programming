#!/bin/bash
# makes request to 0.0.0.0:5000/catch_me causing server to respond with message 
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
