#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) === true || isNaN(b) === true) {
    return NaN;
  } else if (a === undefined) {
    return NaN;
  } else {
    return a + b;
  }
}
trial = add(process.argv[2], process.argv[3]);
console.log(trial);
