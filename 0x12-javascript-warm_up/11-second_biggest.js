#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments.
// You can assume all arguments can be converted to integer
// If no argument passed, print 0
// If the number of arguments is 1, print 0
// You must use console.log(...) to print all output
// You are not allowed to use var

// Printing 0 if the command line argument is 1 or not passed
if (process.argv.length <= 3) {
  console.log(0);
} else {
  // Implementing my solution using an array
  // Storing only the arguments in an array and typecasting them to numbers
  const myArray = process.argv.map(Number).slice(2, process.argv.length).sort((a, b) => a - b); // Sorting and typecasting the numbers
  console.log(myArray[myArray.length - 2]); // Returns the second biggest number.
}
