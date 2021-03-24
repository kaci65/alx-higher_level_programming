#!/usr/bin/node
// function that returns sum of 2 ints
module.exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
