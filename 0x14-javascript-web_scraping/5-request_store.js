#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Retrieve the URL and file path from command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Send a GET request to the specified URL and store the body response in a file
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    // Write the body response to the specified file with UTF-8 encoding
    fs.writeFile(filePath, body, 'utf8', function (err) {
      if (err) {
        console.error(err);
      } else {
        console.log('File saved successfully!');
      }
    });
  }
});
