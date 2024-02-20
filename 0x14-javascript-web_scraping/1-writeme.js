#!/usr/bin/node

const fs = require('fs');

// Retrieve the file path and string to write from command-line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the content to the specified file
fs.writeFile(filePath, content, 'utf8', function (error) {
  if (error) {
    console.error(error);
  }
});
