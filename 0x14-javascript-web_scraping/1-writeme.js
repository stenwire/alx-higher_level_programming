#!/usr/bin/node

const fs = require('fs');
const myArgs = process.argv.slice(2);

function checkErr (err) {
  if (err) {
    console.log(err);
  }
}

function main () {
  const writeStream = fs.createWriteStream(myArgs[0]);
  writeStream.write(myArgs[1], 'utf8', checkErr);
  writeStream.end();
}

main();
