#!/usr/bin/node
const myChar = 'X';
const argLength = process.argv.length - 2;
const argument = process.argv[2];
if (argLength <= 0) {
  console.log('Missing size');
} else if (isNaN(argument)) {
  console.log('Missing size');
} else if (argument < 0) {
  process.exit(1);
} else {
  for (let i = 0; i < argument; i++) {
    for (let j = 0; j < argument; j++) {
      process.stdout.write(myChar);
    }
    console.log('');
  }
}
