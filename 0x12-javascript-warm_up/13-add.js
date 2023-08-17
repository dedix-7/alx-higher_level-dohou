#!/usr/bin/node
// A function that returns the addition of 2 integers.
// The function must be visible from outside
// The name of the function must be add
// You are not allowed to use var
function add (a, b) {
  a = Math.floor(Number(a)); // Typecasting and rounding off to a number
  b = Math.floor(Number(b)); // Typecasting and rounding off to a number

  return a + b;
}
exports.add = (a, b) => add(a, b); // Exporting the function
