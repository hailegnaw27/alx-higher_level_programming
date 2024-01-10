#!/usr/bin/node

const languages = ["C", "Python", "JavaScript"];

for (let i = 0; i < 3; i++) {
  console.log(languages[i] + " is " + getMessage(languages[i]));
}

function getMessage(language) {
  switch (language) {
    case "C":
      return "fun";
    case "Python":
      return "cool";
    case "JavaScript":
      return "amazing";
    default:
      return "";
  }
}
