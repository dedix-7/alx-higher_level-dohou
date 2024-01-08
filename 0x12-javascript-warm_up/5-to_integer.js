#!/usr/bin/node
// A script that prints: My number: <first argument converted in integer>
// If the first argument can be converted to an integer.
// If the argument can’t be converted to an integer, print “Not a number”
// You must use console.log(...) to print all output
// You are not allowed to use var
// You are not allowed to use try/catch
const num = process.argv[2]; // Storing first argument
const intNum = Number(num); // Typecasting to a number
const myNum = Math.floor(intNum); // Rounding off the value of argument
if (isNaN(myNum) === true) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNum}`);
}
