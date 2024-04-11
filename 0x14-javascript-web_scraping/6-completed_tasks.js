#!/usr/bin/node

const request = require('request');
const myURL = process.argv[2];
//
// Getting the API response
request.get(myURL, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const tasksCompleted = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
