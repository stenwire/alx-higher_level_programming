#!/usr/bin/node

/*module.exports = class Rectangle {
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
};*/
module.exports = class Rectangle {

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
  
 };
