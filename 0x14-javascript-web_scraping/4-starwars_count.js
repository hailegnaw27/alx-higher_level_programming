#!/usr/bin/node

const request = require('request');

// Retrieve the API URL from command-line argument
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const characterId = 18;

// Send a GET request to the Star Wars API and count the number of movies where Wedge Antilles is present
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const movieCount = films.filter((film) => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;
    console.log(movieCount);
  }
});
