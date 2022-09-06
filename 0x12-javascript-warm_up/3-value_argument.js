#!/usr/bin/node

const process = require('process');
const args = process.argv;
const argLength = args.length;

if (argLength <= 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
