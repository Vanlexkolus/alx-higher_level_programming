#!/usr/bin/node
//  This is a function that we'll e exporting an make global
function add (a, b) {
  return (a + b);
}
module.exports = { add };
