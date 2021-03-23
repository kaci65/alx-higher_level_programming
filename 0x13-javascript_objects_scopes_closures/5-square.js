#!/usr/bin/node
// class Square defining square and inheriting from Rectangle(4-rectangle.js)
const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
