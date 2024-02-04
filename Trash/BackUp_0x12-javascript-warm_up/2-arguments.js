#!/usr/bin/node
const cmdArgs = process.argv.length - 2;
if (cmdArgs === 0) {
  console.log('No argument');
} else if (cmdArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
