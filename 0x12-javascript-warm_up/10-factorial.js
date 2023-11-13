#!/usr/bin/node
function factorial (n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const number = Number(process.argv[2]);

if (Number.isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}
