#!/usr/bin/node
const firstArgument = Number(process.argv[2]);

if (Number.isNaN(firstArgument) || firstArgument < 1) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArgument; i++) {
    console.log('C is fun');
  }
}
