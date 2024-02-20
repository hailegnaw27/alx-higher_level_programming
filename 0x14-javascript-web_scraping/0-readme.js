#!/usr/bin/node

const fs = require('fs');

// Read and display the content of the specified file
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
