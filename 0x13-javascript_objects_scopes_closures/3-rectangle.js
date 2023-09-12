#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      const emptyRectangle = Object.create(Rectangle.prototype);
      return emptyRectangle;
    }
    this.width = w;
    this.height = h;
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
}

module.exports = Rectangle;
