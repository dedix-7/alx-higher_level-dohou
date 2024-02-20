#!/usr/bin/node
function factorial (a) {
  if (a === undefined || isNaN(a) === true || a === 1) {
    return 1;
  } else {
    // Calling the factorial function recursively, like in C
    return a * factorial(a - 1);
  }
}
console.log(factorial(Math.floor(Number(process.argv[2]))));
