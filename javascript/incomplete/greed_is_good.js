// Greed is a dice game played with five six-sided dice. 
// Your mission, should you choose to accept it, is to score a 
// throw according to these rules. 
// 
// You will always be given an array with five six-sided dice values.
// 
// Three 1's => 1000 points
// Three 6's =>  600 points
// Three 5's =>  500 points
// Three 4's =>  400 points
// Three 3's =>  300 points
// Three 2's =>  200 points
// One   1   =>  100 points
// One   5   =>   50 point
//
// 
// A single die can only be counted once in each roll. 
// For example, a given "5" can only count as part of a 
// triplet (contributing to the 500 points) or as a single 50 points, 
// but not both in the same roll.
//
// Example scoring
// 
//  Throw       Score
//  ---------   ------------------
//  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
//  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
//  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
//
//  In some languages, it is possible to mutate the input to the function. 
//  This is something that you should never do.
//  If you mutate the input, you will not be able to pass all the tests.
//

const score = ( dice ) => {
  // points = { 1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200 }
  let total = 0;
  let points = 0;
  const map = dice.reduce((acc, e) => acc.set(e, (acc.get(e) || 0) + 1), new Map());
  items = [...map.entries()]
  // console.log(items)
  // for (const {key, value} in items) {
  //   if (value >= 3) {
  //     total += items[key] * Math.floor(value)
  //   }
  //   if (key === 1) {
  //     total += 100 * (value % 3)
  //   } else if (key === 5) {
  //     total += 50 * (value % 3)
  //   }
  // }
  // return total;
  items.forEach((item) => {
    // if (item[0] === 1 && item[1] === 4) {
    //   points += 100;
    //   item[1] = 3;
    // }
    // if (item[0] === 5 && item[1] === 4) {
    //   points += 50;
    //   item[1] = 3;
    // }
    if (item[0] === 1 && item[1] === 3) {
      points += 1000;
    }
    if (item[0] === 6 && item[1] === 3) {
      points += 600;
    }
    if (item[0] === 5 && item[1] === 3) {
      points += 500;
    }
    if (item[0] === 4 && item[1] === 3) {
      points += 400;
    }
    if (item[0] === 3 && item[1] === 3) {
      points += 300;
    }
    if (item[0] === 2 && item[1] === 3) {
      points += 200;
    }
    if (item[0] === 1 && item[1] === 1) {
      points += 100;
    }
    if (item[0] === 5 && item[1] === 1) {
      points += 50;
    }
  })
  return points
}

// TESTS
console.log( "----------------------------Scorer Function----------------------------");

console.log( "should value this as worthless");
console.log(score( [2, 3, 4, 6, 2] ) == 0,   "Should be 0 :-(" );

console.log( "should value this triplet correctly");
console.log( score( [4, 4, 4, 3, 3] ) == 400, "Should be 400" );
console.log( score( [4, 4, 3, 3, 3] ) == 400, "Should be 300" );
console.log( score( [1, 1, 1, 3, 1] ) == 1100, "Should be 1100" );

console.log( "should value this mixed set correctly");
console.log( score( [2, 4, 4, 5, 4] ) == 450, "Should be 450" );
