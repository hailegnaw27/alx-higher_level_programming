#!/usr/bin/node

const request = require('request');

// Retrieve the URL to request from command-line argument
const url = process.argv[2];

// Send a GET request to the specified URL and display the status code
request(url, function (error, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
