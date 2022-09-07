#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this.Rectangle;
    } else {
      this.width = w,
      this.height = h
    }
  }
  print = function () {
    let myStr = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        myStr += 'X';
      }
      console.log(myStr);
      myStr = '';
    }
  }
  rotate = function () {
    let temp = null;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
    this.height = this.height;
  }
  double = function () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
