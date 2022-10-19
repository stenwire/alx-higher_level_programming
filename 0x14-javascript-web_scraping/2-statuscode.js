#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);

request(myArgs[0], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
