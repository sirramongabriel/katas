// Convert number to reversed array of digits
//
// 8 kyu
//
// Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
//
// Example(Input => Output):
// 348597 => [7,9,5,8,4,3]
// 0 => [0]

const digitize = (number) => {
  digits = number.toString();
  digitsStringArray = digits.split("");
  const digitsNumberArray = digitsStringArray.map((stringDigit) => Number(stringDigit));
  const result = digitsNumberArray.reverse();
  return result;
}

//
// Tests
//
console.log(digitize(35231), "Should equal [1,3,2,5,3]");
console.log(digitize(0),"Should equal [0]");