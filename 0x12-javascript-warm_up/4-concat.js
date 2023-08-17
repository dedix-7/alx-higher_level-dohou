#!/usr/bin/node
// A script that prints two arguments passed to it
// in the following format: " is "
const firstArg = process.argv[2];
const secondArg = process.argv[3];
if (firstArg === undefined && secondArg === undefined) {
  console.log(`${typeof firstArg} is ${typeof secondArg}`);
} else if (secondArg === undefined) {
  console.log(`${firstArg} is ${typeof secondArg}`);
} else {
  console.log(`${firstArg} is ${secondArg}`);
}
