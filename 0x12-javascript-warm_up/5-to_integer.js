#!/usr/bin/node
// print text if argument can be converted to int
const numInt = Number(process.argv[2]);
if (Number.isNaN(numInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numInt);
}
