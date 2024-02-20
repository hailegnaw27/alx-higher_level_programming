#!/usr/bin/node

const request = require('request');

// Retrieve the movie ID from command-line argument
const movieId = process.argv[2];

// Construct the API URL using the provided movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send a GET request to the Star Wars API to retrieve movie details
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);

    // Retrieve the character URLs from the movie in the same order as the "characters" field
    const characterUrls = movie.characters;

    // Create a counter variable to keep track of the number of characters processed
    let charactersProcessed = 0;

    // Iterate through the character URLs and send GET requests to retrieve character details
    characterUrls.forEach(function (characterUrl) {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(body);

          // Extract and print the character name
          console.log(character.name);

          // Increase the counter variable
          charactersProcessed++;

          // Check if all characters have been processed
          if (charactersProcessed === characterUrls.length) {
            // All characters have been processed, exit the program
            process.exit();
          }
        }
      });
    });
  }
});
