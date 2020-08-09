//-----------------
// Description: Not finished...
//-----------------
//
// Wnen provided a triplet (an array of 3 numbers)
//  - map & sort triplet
//  - store value of number in the middle
//  - check value againts origional array
//  - return origional array's indicie where value is located
//
// var gimme = function (inputArray) {
//   Implement this function
// };
//
// Test.assertEquals(gimme([2, 3, 1]), 0, 'Finds the index of middle element');
// Test.assertEquals(gimme([5, 10, 14]), 1, 'Finds the index of middle element')
// Test.assertEquals(gimme([5.3, 10.67, 14.354]), 1, 'Finds the index of middle element')
//
// Array#sort
//
// #sort((a, b) => a - b);
//

var gimme = function (inputArray) {
  let array = inputArray.sort;

  let middleNumber = array[1];

  // let original_indicie = 0;

  inputArray.forEach(num => {
    if (num === middleNumber) {
      let original_indicie = inputArray.findIndex(num);
    }
  })
  return original_indicie;
};
