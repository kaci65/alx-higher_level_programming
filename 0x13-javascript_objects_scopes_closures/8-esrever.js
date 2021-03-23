#!/usr/bin/node
// Function to reverse a list and return it
exports.esrever = function (list) {
  let leftAux = 0;
  let rightAux = list.length - 1;
  
  while (leftAux < rightAux) {
    let tmp = list[leftAux];
    list[leftAux] = list[rightAux];
    list[rightAux] = tmp;
    leftAux++;
    rightAux--;
  }
  return list;
};
