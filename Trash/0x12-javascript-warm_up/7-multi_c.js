#!/usr/bin/node
// A script that prints x times “C is fun”
// Where x is the first argument of the script
// If the first argument can’t be converted to an integer, print “Missing number of occurrences”
// You must use console.log(...) to print all output
// You are not allowed to use var
// You can use only two console.log
// You must use a loop (while, for, etc.)
const commLineArg = Math.floor(Number(process.argv[2]));
const myArray = ['C is fun'];
let printStatement = '';
if (isNaN(commLineArg) === true) {
  console.log('Missing number of occurrences');
} else {
  let d; // We will use this to print in our loops
  for (d = 0; d < commLineArg; d++) {
    for (printStatement of myArray) {
      console.log(printStatement);
    }
  }
}
