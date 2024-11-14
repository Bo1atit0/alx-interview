#!/usr/bin/node

// Write a script that prints all characters of a Star Wars movie:
// The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name per line in the same order as the “characters” list in the /films/ endpoint
// You must use the Star wars API
// You must use the request module

// moviebody -> charactersArray -> charactersUrl -> charactersName

const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to Fetch Data:', ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}
makeRequest(movieUrl)
  .then(movieBody => {
    const charactersObject = movieBody.characters.map(charactersUrl => makeRequest(charactersUrl));
    return Promise.all(charactersObject);
  }
  )
  .then(characterName => {
    characterName.forEach(characters => {
      console.log(characters.name);
    });
  });
