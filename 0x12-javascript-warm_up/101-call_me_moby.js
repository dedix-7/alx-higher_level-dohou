#!/usr/bin/node
exports.callMeMoby = function (x, recallFunction) {
  for (let i = 0; i < x; i++) {
    recallFunction();
  }
};
