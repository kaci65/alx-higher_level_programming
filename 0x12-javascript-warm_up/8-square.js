#!/usr/bin/node
// print square using argument
const size_int = Number(process.argv[2]);
if (Number.isNaN(size_int)) {
  console.log("Missing size");
} else {
    for (let i = 0; i < size_int; i++) {
      for (let j = 0; j < size_int; j++) {
        process.stdout.write("X");
      }
      console.log();
    }
}
