#!/usr/bin/node

const process = require('process');
const args = process.argv;
const argLength = args.length;

if (argLength <= 2) {
  console.log('Missing number of occurrences');
} else if (isNaN(Number(args[2]))) {
  console.log('Missing number of occurrences');
} else {
  let count = 0;
  while (count < args[2]) {
    console.log('C is fun');
    count++;
  }
}
