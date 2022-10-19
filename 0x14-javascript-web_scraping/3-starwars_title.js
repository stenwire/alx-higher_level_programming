#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const myURL = `https://swapi-api.hbtn.io/api/films/${myArgs[0]}`;

request(myURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
