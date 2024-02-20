/*
  File: 0-readme.js
  Description: A simple JavaScript file for reading and displaying the content of a Readme file.
  Author: Your Name
  Date: Current Date
*/

const fs = require('fs');

// Function to read and display the content of a Readme file
function readReadmeFile() {
  fs.readFile('README.md', 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading the Readme file:', err);
    } else {
      console.log('Readme file content:\n', data);
    }
  });
}

// Call the function to read the Readme file
readReadmeFile();
