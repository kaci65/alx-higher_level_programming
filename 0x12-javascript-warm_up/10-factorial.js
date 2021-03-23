#!/usr/bin/node
// print factorial from argument
function myFactorial (num) {
  if (Number.isNaN(num)) {
    return (1);
  } else if (num === 0) {
    return (1);
  } else {
    return (num * myFactorial(num - 1));
  }
}
const numInt = Number(process.argv[2]);
console.log(myFactorial(numInt));
