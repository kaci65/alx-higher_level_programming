#!/usr/bin/node
// class Square defining square and inheriting from Square(5-square.js)
const Square = require('./5-square.js');

module.export = class Square extends Square {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('C');
        }
        console.log();
      }
    } else {
        process.stdout.write('X');
    }
  }
};
