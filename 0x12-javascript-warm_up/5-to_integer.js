#!/usr/bin/node

const process = require('process');
const args = process.argv;
const argLength = args.length;

if (argLength <= 2) {
  console.log('Not a number');
} else if (isNaN(Number(args[2]))) {
  console.log('Not a number');
} else {
  console.log(Math.floor(Number(args[2])));
}
