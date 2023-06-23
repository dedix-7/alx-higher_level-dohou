#!/usr/bin/node

const fs = require('fs');
const myFile = process.argv[2];

fs.readFile(myFile, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
