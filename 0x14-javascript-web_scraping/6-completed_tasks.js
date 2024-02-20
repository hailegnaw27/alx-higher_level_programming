#!/usr/bin/node

const request = require('request');

// Retrieve the API URL from command-line argument
const apiUrl = process.argv[2];

// Send a GET request to the provided API URL and compute the number of tasks completed by user id
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};

    // Iterate through the tasks and count the completed tasks for each user id
    tasks.forEach(function (task) {
      if (task.completed) {
        if (completedTasks.hasOwnProperty(task.userId)) {
          completedTasks[task.userId] += 1;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    });

    console.log(completedTasks);
  }
});
