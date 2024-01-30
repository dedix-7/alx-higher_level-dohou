#!/usr/bin/node
const cmdArgs = process.argv[2];
if (cmdArgs === undefined) {
  console.log('No argument');
} else {
  console.log(cmdArgs);
}
