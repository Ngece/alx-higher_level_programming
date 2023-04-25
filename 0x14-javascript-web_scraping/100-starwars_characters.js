#!/usr/bin/node
/*  prints all characters of a Star Wars movie:
    The first argument is the Movie ID 
    Displays one character name by line
*/

const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
