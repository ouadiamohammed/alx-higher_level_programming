#!/usr/bin/node
const firstArgument = process.argv[2];
const convertedNumber = Number(firstArgument);

if (Number.isInteger(convertedNumber)) {
  console.log(`My number: ${convertedNumber}`);
} else {
  console.log('Not a number');
}
