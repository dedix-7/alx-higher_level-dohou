#!/usr/bin/node
// A script that prints a square
// The first argument is the size of the square
// If the first argument can’t be converted to an integer, print “Missing size”
// You must use the character X to print the square
// You must use console.log(...) to print all output
// You are not allowed to use var
// You must use a loop (while, for, etc.)
const commLineArg = Math.floor(Number(process.argv[2]));
if (isNaN(commLineArg) === true) {
  console.log('Missing size');
} else {
  for (let column = 0; column < commLineArg; column++) {
    let row = '';
    // This line declares another for loop that iterates r from 0 to size - 1, incrementing r
    // by 1 on each iteration. Inside the loop, it appends the character "X" to the row string.
    for (let r = 0; r < commLineArg; r++) row = row + 'X';
    console.log(row);
  }
}
