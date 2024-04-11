#!/usr/bin/node
const request = require('request');
const fileIO = require('fs');
const myURL = process.argv[2];
const fileToWriteTo = process.argv[3];
//
// Getting the API response
request(myURL, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  fileIO.writeFile(fileToWriteTo, body, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    }
  });
});
