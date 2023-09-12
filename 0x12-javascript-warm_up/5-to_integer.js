#!/usr/bin/node

const firstArgument = parseInt(process.argv[2]);

if (!isNaN(firstArgument)) {
  console.log(`My number: ${firstArgument}`);
} else {
  console.log('Not a number');
}
