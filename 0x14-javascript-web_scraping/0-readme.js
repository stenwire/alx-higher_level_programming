#!/usr/bin/node

const fs = require('fs');
const myArgs = process.argv.slice(2);

function readData (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
}

function main () {
  fs.readFile(myArgs[0], 'utf8', readData);
}

main();
