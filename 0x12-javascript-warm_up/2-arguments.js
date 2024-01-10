#!/usr/bin/node

const argsCount = process.argv.length;

if (argsCount === 2) {
  console.log("Argument found");
} else if (argsCount > 2) {
  console.log("Arguments found");
} else {
  console.log("No argument");
}
