#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const H = this.height;
    const W = this.width;
    for (let dan = 0; dan < H; dan++) {
      let char = '';
      for (let fav = 0; fav < W; fav++) {
        // console.log('X');
        // process.stdout.write('X');
        char = char + 'X';
      }
      console.log(char);
    }
  }

  double () {
    const H = this.height * 2;
    const W = this.width * 2;
    for (let dan = 0; dan < H; dan++) {
      let char = '';
      for (let fav = 0; fav < W; fav++) {
        // console.log('X');
        // process.stdout.write('X');
        char = char + 'X';
      }
      console.log(char);
    }
  }

  rotate () {
    const H = this.height * 2;
    const W = this.width * 2;
    for (let fav = 0; fav < W; fav++) {
      let char = '';
      for (let dan = 0; dan < H; dan++) {
        // console.log('X');
        // process.stdout.write('X');
        char = char + 'X';
      }
      console.log(char);
    }
  }
};
