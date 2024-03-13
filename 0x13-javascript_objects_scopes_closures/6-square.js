#!/usr/bin/node
/*  Write a class Square that defines a square and inherits from Square of 5-square.js:

    You must use the class notation for defining your class and extends
    Create an instance method called charPrint(c) that prints the rectangle using the character c
        If c is undefined, use the character X
*/
const inherSquare = require('./5-square');
class Square extends inherSquare {
  charPrint (c) {
    if (c) {
      let prints = '';
      for (let cont = 0; cont < this.height; cont++) {
        for (let cont = 0; cont < this.height; cont++) {
          prints = prints + c;
        }
        console.log(prints);
        prints = '';
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
