#!/usr/bin/node

const numbers = process.argv.slice(2).map(Number);

if (numbers.length < 2) {
  console.log(0);
} else {
  const sortedNumbers = numbers.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}
