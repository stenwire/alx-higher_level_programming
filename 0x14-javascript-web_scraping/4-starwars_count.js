#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const myURL = `${myArgs[0]}`;


request(myURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i <= res.length; i++) {
      for (var key in res[i]) {
        if (key === 'characters') {
          for (let j = 0; j < res[i].characters.length; j++) {
            if (res[i].characters[j].includes('18')) {
              count += 1;
            }
          }
        }
      }
    }
    console.log(count);
  }
});
