#!/usr/bin/node
const myString = 'C is fun';
const argLength = process.argv.length - 2;
const argument = process.argv[2];
if (argLength <= 0) {
  console.log('Missing number of occurences');
} else if (argument < 0) {
  process.exit(1);
} else {
  for (let i = 0; i < argument; i++) {
    console.log(myString);
  }
}
