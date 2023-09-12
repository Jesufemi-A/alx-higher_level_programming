#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const integers = args.map(Number).sort((a, b) => b - a);

  // Find the second largest integer
  const secondLargest = integers[1];

  console.log(secondLargest);
}
