#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);
if (isNaN(squareSize)) {
  console.log('Missing Size');
} else {
  for (let i = 0; i < squareSize; i++) {
    for (let j = 0; j < squareSize; j++) {
      console.log('X');
    }
  }
}
