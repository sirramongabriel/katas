// Reduce but grow
//
// 8 kyu
//
// Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

//
// Example:
//
// [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

const grow = (array) => {
  const result = array.reduce((a, b) => a * b);
  return result;
};

// 
// Tests
// 
console.log(grow([1, 2, 3]), 6);
console.log(grow([4, 1, 1, 1, 4]), 16); 
console.log(grow([2, 2, 2, 2, 2, 2]), 64); 