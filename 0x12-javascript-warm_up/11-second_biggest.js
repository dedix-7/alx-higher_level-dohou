#!/usr/bin/node
// Check the number of arguments
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const myArr = process.argv.map(Number).slice(2, process.argv.length).sort((a, b) => a - b);
  console.log(myArr.length - 2);
}
