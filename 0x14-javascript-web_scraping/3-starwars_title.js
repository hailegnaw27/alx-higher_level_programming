#!/usr/bin/node

const request = require('request');

// Retrieve the movie ID from command-line argument
const movieID = process.argv[2];

// Construct the API endpoint URL
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Send a GET request to the Star Wars API and retrieve the movie title
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
