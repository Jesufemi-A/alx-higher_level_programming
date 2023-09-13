#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let elementCount = 0;

  for (const element of list) {
    if (element === searchElement) {
      elementCount++;
    }
  }

  return elementCount;
};
