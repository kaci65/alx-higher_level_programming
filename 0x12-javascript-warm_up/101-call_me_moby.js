#!/usr/bin/node
// function that returns sum of 2 ints
module.exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
};
