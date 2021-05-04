#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');
if (process.argv.length === 3) {
  const filmID = process.argv[2];
  const url = 'https://swapi-api.hbtn.io/api/films/' + filmID;
  request(url, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).title);
    }
  });
}
