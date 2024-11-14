// Write a script that prints all characters of a Star Wars movie:
// The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name per line in the same order as the “characters” list in the /films/ endpoint
// You must use the Star wars API
// You must use the request module

const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  }

  const movieBody = JSON.parse(body);
  // console.log(movieBody)

  const characters = movieBody.characters;
  characters.forEach(charactersUrl => {
    request(charactersUrl, (error, response, body) => {
      if (error) {
        console.log('Error:', error);
      }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  });
});
