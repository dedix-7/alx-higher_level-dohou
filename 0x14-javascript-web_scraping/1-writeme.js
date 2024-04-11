#!/usr/bin/node
const fileIO = require('fs');
const contentToWrite = String(process.argv[3]);
fileIO.writeFile(process.argv[2], contentToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
  // console.log();
});
