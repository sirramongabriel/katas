//-----------------
// Description:
//-----------------
// Given a target number and an array of numbers
// locate two numbers.values === target
// return the indicies of these values to a new array
//
// function numericalCompare(a, b) {
//   return a - b;
// }
//
// console.log(twoSum([1,2,3], 4).sort(numericalCompare), [0,2]);
// console.log(twoSum([1234,5678,9012], 14690).sort(numericalCompare), [1,2]);
// console.log(twoSum([2,2,3], 4).sort(numericalCompare), [0,1]);

function twoSum(numbers, target) {
  let components = [];
  for (let num=0;num<=numbers.length;num++) {
    for (let numPlus=(num+1);numPlus<=numbers.length;numPlus++) {
      if (numbers[num] + numbers[numPlus] === target) {
        components.push(num, numPlus);
      }
    }
  }
  return components;
}

function numericalCompare(a, b) {
  return a - b;
}

console.log(twoSum([1,2,3], 4).sort(numericalCompare), [0,2]);
console.log(twoSum([1234,5678,9012], 14690).sort(numericalCompare), [1,2]);
console.log(twoSum([2,2,3], 4).sort(numericalCompare), [0,1]);

components: {
  componentName
}
components: {

  comment
}
