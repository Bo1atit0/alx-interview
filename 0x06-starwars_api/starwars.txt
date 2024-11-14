const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// URL for fetching the movie details from the Star Wars API
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch movie data
request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log('Failed to fetch movie data:', response.statusCode);
    return;
  }

  // Parse the movie data
  const movieData = JSON.parse(body);

  // Check if characters exist in the movie data
  if (!movieData.characters || movieData.characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  // Print all character names from the characters list
  movieData.characters.forEach(characterUrl => {
    request(characterUrl, (err, res, charBody) => {
      if (err) {
        console.error('Error fetching character data:', err);
        return;
      }

      if (res.statusCode !== 200) {
        console.log('Failed to fetch character data:', res.statusCode);
        return;
      }

      // Parse and print the character's name
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
