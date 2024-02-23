#!/usr/bin/node
let functionCall = -1;
exports.logMe = function (item) {
  functionCall++; // This cariable increases everytime the function is called
  console.log(`${functionCall}: ${item}`);
};
