#!/usr/bin/node
// A function that returns the reversed version of a list:
// // Prototype: exports.esrever = function (list)
// // You are not allow to use the built-in method reverse

exports.esrever = function (list) {
  // The easy way
  // return list.reverse();

  // Do this the Hard Way!
  // Declaring variables
  const myRevArray = [];
  let myArrObject;
  let arrNum = 0;
  const arrLen = list.length;
  let d;

  for (d = arrLen - 1; d >= 0; d--) {
    myArrObject = list[d];
    myRevArray[arrNum] = myArrObject;
    arrNum++;
  }

  /*
  do {
    myArrObject = list[list.length - 1];
    myRevArray[d] = myArrObject;
    d++;
  } while (arrLen--);
  */

  return myRevArray;
};
