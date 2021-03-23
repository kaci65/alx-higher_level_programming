#!/usr/bin/node
// create an empty object if h or w === 0 or < 0
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
