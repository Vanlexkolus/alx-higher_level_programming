#!/usr/bin/node
//  This script print's the arguments that are being passed to it
const myArg = process.argv.length;
const i = 2;
if (myArg <= 2) {
  console.log('No argument');
} else if (myArg > 2) {
  console.log(process.argv[i]);
}
