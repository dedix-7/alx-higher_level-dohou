#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nb = 0;
  const listLength = list.length;
  for (let i = 0; i < listLength; i++) {
    if (list[i] === searchElement) {
      nb++;
    }
  }
  return nb;
};
