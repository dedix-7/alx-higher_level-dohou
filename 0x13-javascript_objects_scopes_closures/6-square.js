#!/usr/bin/node
// A class Square that defines a square and inherits from Square of 5-square.js:
// You must use the class notation for defining your class and extends
// Create an instance method called charPrint(c) that prints the rectangle using the character c
// If c is undefined, use the character X
//
// 'use strict';
const mySquare = require('./5-square.js');
module.exports = class Square extends mySquare {
  /*
  constructor () {
    super();
  }
  */

  charPrint (c) {
    /* if (arguments[0] === undefined) { super.print (); } */
    const H = this.height;
    const W = this.width;
    if (c === undefined) {
      for (let dan = 0; dan < H; dan++) {
        let char = '';
        for (let fav = 0; fav < W; fav++) {
          char = char + 'X';
        }
        console.log(char);
      }
    } else {
      for (let dan = 0; dan < H; dan++) {
        let char = '';
        for (let fav = 0; fav < W; fav++) {
          char = char + c;
        }
        console.log(char);
      }
    }
  }
};
