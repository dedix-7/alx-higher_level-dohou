#!/usr/bin/bash
exports.esrever = function (list) {
  const listLength = list.length;
  let indexNumber = 0;
  const myReversedArray = [];
  let myArrayObject;
  for (let i = listLength - 1; i >= 0; i--) {
    myArrayObject = list[i];
    myReversedArray[indexNumber] = myArrayObject;
    indexNumber++;
  }
  return myReversedArray;
};
