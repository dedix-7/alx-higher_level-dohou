#!/usr/bin/node
const length = process.argv.length - 2;
const firstArg = process.argv[2];
const secondArg = process.argv[3];
if (length <= 0) {
  console.log('undefined is undefined');
} else if (length === 1) {
  console.log(`${firstArg} is undefined`);
} else {
  console.log(`${firstArg} is ${secondArg}`);
}
