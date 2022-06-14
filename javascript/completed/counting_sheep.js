// Counting sheep 
// 
// 8 kyu
// 
// Consider an array/list of sheep where some sheep may be missing from their place. 
// We need a function that counts the number of sheep present in the array (true means present).
// 
// Example,
// 
// [true,  true,  true,  false,
//   true,  true,  true,  true ,
//   true,  false, true,  false,
//   true,  false, false, true ,
//   true,  true,  true,  true ,
//   false, false, true,  true]
// 
// The correct answer would be 17.
// 
// Hint: Don't forget to check for bad values like null/undefined

const countSheeps = (sheeps) => {
  const sheepPresent = [];
  sheeps.map((sheep) => {
    if (sheep === true) {
      sheepPresent.push('sheep');
    }
  });
  const result = sheepPresent.length
  return result;
};

//
// Tests
//
let testArray = [true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true ];
  
console.log(countSheeps(testArray), 17, "There are 17 sheeps in total")