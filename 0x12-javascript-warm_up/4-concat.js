#!/usr/bin/node

const process = require('process');
const args = process.argv;
const argLength = args.length;

if (argLength <= 2) {
  console.log('undefined is undefined');
} else if (argLength === 3) {
  console.log(`${args[2]} is undefined`);
} else {
  console.log(`${args[2]} is ${args[3]}`);
}
