#!/usr/bin/node
// print sum of two ints
function add (a, b) {
  const sum = a + b;
  console.log(sum)
}
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);
add(a, b);
