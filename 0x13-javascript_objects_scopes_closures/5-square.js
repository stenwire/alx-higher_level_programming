#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size, w, h) {
    super(w, h)
    this.size = size
  }
  print = function () {
    let myStr = '';
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        myStr += 'X';
      }
      console.log(myStr);
      myStr = '';
    }
  }
  double = function () {
    this.size = this.size * 2;
  }
};
