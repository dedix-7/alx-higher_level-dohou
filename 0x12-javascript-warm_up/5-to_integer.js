#!/usr/bin/node
const length = process.argv.length - 2;
const firstArg = Number(Math.floor(process.argv[2]));
if (length <= 0) {
  console.log('Not a number');
} else if (isNaN(Number(firstArg))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${firstArg}`);
}
