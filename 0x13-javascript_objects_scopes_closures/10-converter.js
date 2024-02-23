#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    const flooredNumber = Math.floor(number);
    return flooredNumber.toString(base);
  };
};
