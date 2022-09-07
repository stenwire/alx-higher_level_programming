#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let result = [];
  const listLength = list.length;
  for (let i = 0; i < listLength; i++) {
    if (list[i] === searchElement) {
      result.push(list[i]);
    }
  }
  const resultLength = result.length;
  return resultLength;
}
