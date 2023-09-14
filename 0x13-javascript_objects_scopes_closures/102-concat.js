#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 3) {
  console.error('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const sourceFile1 = args[0];
const sourceFile2 = args[1];
const destinationFile = args[2];

try {
  // Read the contents of the first source file
  const data1 = fs.readFileSync(sourceFile1, 'utf8');

  // Read the contents of the second source file
  const data2 = fs.readFileSync(sourceFile2, 'utf8');

  // Concatenate the contents of the two source files with a newline character in between
  const concatenatedData = data1 + '\n' + data2 + '\n';

  // Write the concatenated data to the destination file
  fs.writeFileSync(destinationFile, concatenatedData);

  console.log(`Contents of ${sourceFile1} and ${sourceFile2} have been concatenated to ${destinationFile}`);
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}
