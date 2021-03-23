#!/usr/bin/node
// print square using argument
const sizeInt = Number(process.argv[2]);
if (Number.isNaN(sizeInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sizeInt; i++) {
    for (let j = 0; j < sizeInt; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
