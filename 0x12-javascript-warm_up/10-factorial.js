#!/usr/bin/node
function factorial (n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const number = parseInt(process.argv[2], 10);

console.log(factorial(number));
