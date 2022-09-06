#!/usr/bin/node

const process = require('process');
const args = process.argv;
const argLength = args.length;
const num = parseInt(argv[2]);

function myFactorial (a) {
  if (argLength <= 2 || Number.isNaN(num) {
    return 1;
  } else {
    let answer = 1;
    let i = a;
    while (i >= 1) {
      answer = myFactorial(i);
      i--;
    }
    return answer * i;
  }
}




