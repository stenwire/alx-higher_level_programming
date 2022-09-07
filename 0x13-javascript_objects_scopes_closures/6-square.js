#!/usr/bin/node
const Rectangle = require('./5-square');

// +++++++++++++++++++++++++++++++++++

class Square extends Square {
  constructor(size, mySize) {
    super(size)
    this.mySize = mySize
  }
  charPrint = function (c) {
    if (c) {
      let print = function () {
        let myStr = '';
        for (let i = 0; i < this.mySize; i++) {
          for (let j = 0; j < this.mySize; j++) {
            myStr += 'X';
          }
          console.log(myStr);
          myStr = '';
        }
      }
    } else {
      let print = function () {
        let myStr = '';
        for (let i = 0; i < this.size; i++) {
          for (let j = 0; j < this.size; j++) {
            myStr += 'C';
          }
          console.log(myStr);
          myStr = '';
        }
      }
    }
  }
}
