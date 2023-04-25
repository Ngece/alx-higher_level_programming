#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/
const characterId = 18;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('API Response:', 'Status Code', response.statusCode);
  } else {
    const films = JSON.parse(body).results;
    const wedgeMovies = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    const numMovies = wedgeMovies.length;
    console.log(`Number of movies where Wedge Antilles appears: ${numMovies}`);
  }
});

