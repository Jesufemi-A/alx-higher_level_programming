#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && typeof w === 'number' && typeof h === 'number') {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; i++) {
        rect += 'X';
      }
      console.log(rect);
      rect = '';
    }
  }

  rotate () {
    const helper = this.width;
    this.width = this.height;
    this.height = helper;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
