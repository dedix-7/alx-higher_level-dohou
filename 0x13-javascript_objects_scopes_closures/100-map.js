#!/usr/bin/node
const importedArray = require('./100-data.js').list;
const newArray = importedArray.map((index, item) => item * index);
console.log(importedArray);
console.log(newArray);
