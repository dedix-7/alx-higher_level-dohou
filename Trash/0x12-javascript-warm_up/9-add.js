#!/usr/bin/node
// A script that prints the addition of 2 integers
// The first argument is the first integer
// The second argument is the second integer
// You have to define a function with this prototype: function add(a, b)
// You must use console.log(...) to print all output
// You are not allowed to use var
function addArguments (arg1, arg2) {
  if (isNaN(arg1) === true || isNaN(arg2) === true) {
    return NaN;
  } else if (arg1 === undefined) {
    return NaN;
  } else {
    return arg1 + arg2;
  }
}
console.log(addArguments(Math.floor(Number(process.argv[2])), Math.floor(Number(process.argv[3]))));
