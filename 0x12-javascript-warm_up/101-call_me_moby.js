#!/usr/bin/node
// A function that executes x times a function.
// The function must be visible from outside
// Prototype: function (x, theFunction)
// You are not allowed to use var

// This makes the function visible from outside.
exports.callMeMoby = function (num, myFunction) {
  let dan;
  for (dan = 0; dan < num; dan++) {
    myFunction(); // Calling the function recursively
  }
};
