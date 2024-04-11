#!/usr/bin/node
const fileIO = require('fs');
// Reading the file
fileIO.readFile(process.argv[2], 'utf-8', (err, fileData) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(fileData);
});
