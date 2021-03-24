#!/usr/bin/node
// class Square defining square and inheriting from Square(5-square.js)
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('C');
        }
        console.log();
      }
    } else {
      this.print();
    }
  }
};
