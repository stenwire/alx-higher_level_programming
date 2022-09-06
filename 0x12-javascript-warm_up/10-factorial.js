#!/usr/bin/node

const process = require('process');
const args = process.argv;
const argLength = args.length;

function myFactorial (a) {
  if (argLength <= 2) {
    console.log(1);
  } else {
    let answer = 1;
    let i = a;
    while (i >= 1) {
      answer *= i;
      i--;
    }
    console.log(answer);
  }
}

myFactorial(args[2]);
