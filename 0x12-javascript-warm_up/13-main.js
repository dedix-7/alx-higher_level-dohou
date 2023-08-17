#!/usr/bin/node
// A script that imports the 'add' function from the 13-add module and assigns it to a variable
const add = require('./13-add').add;
console.log(add(3, 5));
