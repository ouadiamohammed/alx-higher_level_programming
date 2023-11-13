#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const firstArgument = Number(process.argv[2]);
const secondArgument = Number(process.argv[3]);

add(firstArgument, secondArgument);
