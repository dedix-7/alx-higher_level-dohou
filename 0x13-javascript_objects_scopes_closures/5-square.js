#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    // Calling the Rectangle constructor and initializing it with
    // the size constructor of the Square class
    super(size, size);
  }
};
