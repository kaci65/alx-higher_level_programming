#!/usr/bin/node
// function to convert number from base 10 to another base passed as argument
module.exports.converter = function (base) {
  return num => {
    return num.toString(base);
  };
};
