#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    // this.size = size;
  }

  // super.double();
  // super.rotate();

  /*
  print () {
    // const H = this.height;
    // const W = this.width;
    const S = this.size;
    for (let dan = 0; dan < S; dan++) {
      let char = '';
      for (let fav = 0; fav < S; fav++) {
        // console.log('X');
        // process.stdout.write('X');
        char = char + 'X';
      }
      console.log(char);
    }
  }
  */
};

/*
In this code, we define a Square class that extends the Rectangle class.
The Square class has a constructor that takes one argument size, which is
used to call the super() method with size passed as both width and height to
the Rectangle class. This way, the Square class inherits the properties and methods
of the Rectangle class, as specified in the requirements.
*/
