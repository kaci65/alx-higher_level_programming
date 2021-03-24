#!/usr/bin/node
// class Square defining square and inheriting from Square(5-square.js)
const Square1 = require('./5-square.js');

module.exports = class Square extends Square1 {
  charPrint (c = 'X') {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('C');
      }
      console.log();
    }
  }
};
