#!/usr/bin/node
// A function that returns the number of occurrences in a list:
// Prototype: exports.nbOccurences = function (list, searchElement)

exports.nbOccurences = function (list, searchElement) {
  // Initializing my counter to count occurrences
  let myOccur = 0;

  // Iterate through the given list (using the length property) to search for occurrence
  for (let d = 0; d < list.length; d++) {
    // If an occurrence of the searchElement is found in the loop,
    if (list[d] === searchElement) {
      // Increment myOccur
      myOccur++;
    }
  }
  // return statement
  return myOccur;
};
