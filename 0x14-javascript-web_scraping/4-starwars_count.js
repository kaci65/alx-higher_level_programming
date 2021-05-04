#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
if (process.argv.length === 3) {
  const url = process.argv[2];
  const actor = '/api/people/18/';
  let count = 0;
  request(url, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      const numMovies = JSON.parse(body).results;
      for (let i = 0; i < numMovies.length; i++) {
        const starWarsActors = numMovies[i].characters;
        if (starWarsActors.find(elem => elem.includes(actor))) {
          count++;
        }
      }
      console.log(count);
    }
  });
}
