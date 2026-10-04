#!/usr/bin/node
const request = require('request');
const characterId = '18';

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    const count = films.filter((film) =>
      film.characters.some((character) => character.endsWith('/' + characterId + '/'))
    ).length;
    console.log(count);
  }
});
