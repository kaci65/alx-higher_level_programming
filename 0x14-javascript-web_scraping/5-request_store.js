#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
if (process.argv.length === 4) {
  const url = process.argv[2];
  const textFile = process.argv[3];
  request(url, function (err, response, body) {
    if (err) {
      console.error(err);
    } else {
      fs.writeFile(textFile, body, 'utf-8', function (err) {
        if (err) {
          console.error(err);
        }
      });
    }
  });
}
