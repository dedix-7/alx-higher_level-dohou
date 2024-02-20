#!/usr/bin/node
const firstArg = process.argv[2];
let answer = 0;
let i = -1;
if (firstArg === undefined || isNaN(firstArg) === true) {
  console.log(1);
} else {
  for (i = 0; i <= firstArg; i++) {
    answer += i;
  }
  console.log(answer);
}
