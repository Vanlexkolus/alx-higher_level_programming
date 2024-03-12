#!/usr/bin/node
//  this code prints a message depending of the number of arguments passed
const argLen = process.argv.length;
if (argLen <= 2) {
  console.log('No argument');
} else if (argLen === 3) {
  console.log('Argument found');
} else if (argLen > 3) {
  console.log('Arguments found');
}
