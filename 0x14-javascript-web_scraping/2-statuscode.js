#!/usr/bin/node
const request = require('request');
// Making a GET request
request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error;
    return;
  }

  // Displaying the status code, as the task requires
  console.log('code:', response.statusCode);
});
