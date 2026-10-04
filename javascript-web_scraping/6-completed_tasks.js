#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const completed = {};
    for (const task of tasks) {
      if (task.completed) {
        completed[task.userId] = (completed[task.userId] || 0) + 1;
      }
    }
    console.log(completed);
  }
});
