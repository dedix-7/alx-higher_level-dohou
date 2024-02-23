#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    return Math.floor(number).toString(base);
  };
};
