#!/usr/bin/node
// function that prints no. of arguments printed & new argument value
let i = 0;
module.exports.logMe = function (item) {
  console.log(`${i}: ${item}`);
  i++;
};
