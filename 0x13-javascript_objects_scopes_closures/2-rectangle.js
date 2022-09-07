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
};
