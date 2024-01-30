#!/usr/bin/node
// A script that computes and prints a factorial
// The first argument is integer (argument can be cast as integer) used for computing the factorial
// Factorial of NaN is 1
// You must do it recursively
// You must use a function
// You must use console.log(...) to print all output
// You are not allowed to use var

function factorial (arg1) {
  if (isNaN(arg1) === true || arg1 === undefined) {
    return 1;
  } else if (arg1 === 1) {
    return 1;
  } else {
    // Calling the function recursively, like in C
    return arg1 * factorial(arg1 - 1);
  }
}
console.log(factorial(Math.floor(Number(process.argv[2]))));
