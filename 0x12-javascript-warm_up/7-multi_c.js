#!/usr/bin/node
// prints text x number of times
const numInt = Number(process.argv[2]);
if (Number.isNaN(numInt)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < numInt) {
    console.log('C is fun');
    i++;
  }
}
