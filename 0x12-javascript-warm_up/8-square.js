#!/usr/bin/node

const process = require('process');
const args = process.argv;
const argLength = args.length;

if (argLength <= 2) {
  console.log('Missing size');
} else if (isNaN(Number(args[2]))) {
  console.log('Missing size');
} else {
  let myStr = '';
  for (let i = 0; i < args[2]; i++) {
    for (let j = 0; j < args[2]; j++) {
      myStr += 'x';
    }
    console.log(myStr);
    myStr = '';
  }
}
