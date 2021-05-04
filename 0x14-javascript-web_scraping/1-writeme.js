#!/usr/bin/node
// script that writes a string to a file

const fs = require('fs');
if (process.argv.length === 4) {
  const filename = process.argv[2];
  const fileContents = process.argv[3];
  fs.writeFile(filename, fileContents, 'utf-8', function (err) {
    if (err) {
      console.error(err);
    }
  });
}
