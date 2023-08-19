#!/usr/bin/node
// A script that imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence.
// Your script must import dict from the file 101-data.js
// In the new dictionary:
// A key is a number of occurrences
// A value is the list of user ids
// Print the new dictionary at the end

// Importing the dict object from 101-data.js and
// destructuring it ('{ dict }') so as to extract
// the 'dict' property from the imported module directly
const { dict } = require('./101-data.js');
// Create a new dictionary to store user ids indexed by occurrence
const userIdsByOccurrence = {};
// Iterating over each user id in the dict.
for (const userId in dict) { // userId represents the keys in dict
  // console.log(userId);
  const occurrence = dict[userId];
  // console.log(occurrences);
  // console.log();

  // If the occurrence is not a key in the new dictionary, initialize it with an empty array
  if (!userIdsByOccurrence[occurrence]) {
    userIdsByOccurrence[occurrence] = [];
  }
  // Push the userId into the array for the corresponding occurrence
  // This groups user ids by the number of their occurrences.
  userIdsByOccurrence[occurrence].push(parseInt(userId));
}

// Print the new dictionary of user ids by occurrence
console.log(userIdsByOccurrence);
