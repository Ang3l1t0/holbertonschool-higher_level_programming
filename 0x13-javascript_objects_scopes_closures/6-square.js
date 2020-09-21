#!/usr/bin/node

const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    if (typeof c !== 'undefined') {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
