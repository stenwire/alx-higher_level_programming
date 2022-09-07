#!/usr/bin/node
// const Rectangle = require('./5-square');

// +++++++++++++++++++++++++++++++


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
    let temp = null
    temp = this.width
    this.width = this.height
    this.height = temp
    this.height = this.height
  }
  double = function () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};


class SquareD extends Rectangle {
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




// +++++++++++++++++++++++++++++++++++

class Square extends SquareD {
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


const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');