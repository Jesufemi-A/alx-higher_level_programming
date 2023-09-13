#!/usr/bin/node

// Import the dict dictionary from 101-data.js
const { dict } = require('./101-data');

// Create a new dictionary for user ids by occurrence
const usersByOccurrence = {};

// Iterate over the entries in the original dictionary
for (const userId in dict) {
  const occurrence = dict[userId];

  // If the occurrence is not a key in the new dictionary, create an empty array
  if (!usersByOccurrence[occurrence]) {
    usersByOccurrence[occurrence] = [];
  }

  // Add the user id to the corresponding occurrence key in the new dictionary
  usersByOccurrence[occurrence].push(userId);
}

// Print the new dictionary
console.log(usersByOccurrence);
