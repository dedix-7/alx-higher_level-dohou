#!/usr/bin/node
const moduleSquare = require('./5-square.js');
module.exports = class Square extends moduleSquare {
  charPrint (c) {
    const height = this.height;
    const width = this.width;
    if (c === undefined) {
      for (let i = 0; i < height; i++) {
        for (let j = 0; j < width; j++) {
          process.stdout.write('X');
        }
        console.log();
      }
    } else {
      for (let i = 0; i < height; i++) {
        for (let j = 0; j < width; j++) {
          process.stdout.write(c);
        }
        console.log();
      }
    }
  }
};
