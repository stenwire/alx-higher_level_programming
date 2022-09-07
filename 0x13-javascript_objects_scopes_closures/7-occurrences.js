#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let result = []
  const listLength = list.length
  for (let i = 0; i < listLength; i++) {
    if (list[i] === searchElement) {
      result.push(list[i])
    }
    const resultLength = result.length
    return resultLength
  }
}

// exports.nbOccurences = function (list, searchElement);

// const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["S", 12, "c", "S", "School", 8], "S"));
