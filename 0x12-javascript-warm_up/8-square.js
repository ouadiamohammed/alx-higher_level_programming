#!/usr/bin/node
const square = Number(process.argv[2]);

if (Number.isNaN(square)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < square; i++) {
    let line = '';
    for (let j = 0; j < square; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
