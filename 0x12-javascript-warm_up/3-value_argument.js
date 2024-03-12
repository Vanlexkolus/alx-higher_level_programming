#!/usr/bin/node
//  This script print's the arguments that are being passed to it
if (process.argv[2] == undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
