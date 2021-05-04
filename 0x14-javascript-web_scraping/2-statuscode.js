#!/usr/bin/node
// script that display the status code of a GET request

const request = require('request');
if (process.argv.length === 3) {
  const url = process.argv[2];
  request
    .get(url)
    .on('response', function (response) {
      console.log('code:', response.statusCode);
    });
  request
    .get(url)
    .on('error', function (err) {
      console.error(err);
    });
}
