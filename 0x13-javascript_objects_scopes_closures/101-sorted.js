#!/usr/bin/node
const dict = require('./101-data.js').dict;
// Create an array of dictionary values
// const dictValues = [];
// for (let key in dict) {
//   let value = dict[key];
//   dictValues.push(value); // Using the push method
// }
// Sort the keys and coonvert back to an array
// const uniqueValues = new Set(dictValues);
// const sortedValues = Array.from(uniqueValues)
// console.log(sortedValues);
// Create an empty dictionary to store the keys
const sortedKeysByValues = {};
// Sort the dictionary using the sortedValues
for (const key in dict) {
  const value = dict[key];
  // Initialize an empty array if the value is not a key in the new dictionary
  if (!sortedKeysByValues[value]) {
    sortedKeysByValues[value] = []; // Initialize an empty array
  }
  sortedKeysByValues[value].push(parseInt(key));
}
console.log(sortedKeysByValues);
