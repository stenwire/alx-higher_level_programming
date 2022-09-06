#!/usr/bin/node

const process = require('process');
const args = process.argv;
const argLength = args.length;

function add (a, b) {
  if (argLength <= 3) {
    console.log('NaN');
  } else {
    const mySum = Number(a) + Number(b);
    console.log(mySum);
  }
}

const a = args[2];
const b = args[3];
add(a, b);
