#!/usr/bin/node
/* prints all characters of a Star Wars movie:
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi” 
 * Displays one character name by line in the same order 
 * of the list “characters” in the /films/ response
 *
 */

const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    let characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}

