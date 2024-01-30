#!/usr/bin/node
// A function that increments and calls a function.
// The function must be visible from outside
// Prototype: function (number, theFunction)
// You are not allowed to use var

exports.addMeMaybe = function (num, myFunction) { // Making the function visible from outside
  myFunction(++num); // Incrementing the number by 1.
};
