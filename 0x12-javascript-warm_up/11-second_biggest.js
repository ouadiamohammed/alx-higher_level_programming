#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

args.sort((a, b) => b - a);

console.log(args[1] || 0);
