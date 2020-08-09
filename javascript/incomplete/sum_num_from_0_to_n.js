//-----------------
// Description:
//-----------------
// We want to generate a function that computes the series
// starting from 0 and ending until the given number
// following the sequence:
//
// 0 1 3 6 10 15 21 28 36 45 55 ....
//
// which is created by
//
// 0, 0+1, 0+1+2, 0+1+2+3, 0+1+2+3+4, 0+1+2+3+4+5, 0+1+2+3+4+5+6, 0+1+2+3+4+5+6+7 etc..
//-----------------
//

// var SequenceSum = (function() {
//   function SequenceSum() {}
//
//   SequenceSum.showSequence = function(count) {
//     for (i=0;i<=count;i++) {
//
//     }
//   };
//
//   return SequenceSum;
//
// })();

var SequenceSum = (function() {
  function SequenceSum() {}
  SequenceSum.showSequence = function(number) {
    let sequence = 0;
    let count = 0;
    let string = '';
    if (Math.sign(number)===-1) {
        string = number + "<0";
        return string;
      } else if (Math.sign(number)===0) {
        string = "0=0";
        return string;
      }
    for (i=0;i<=(number);i++) {
      count += sequence;
      if (i < 1 && Math.sign(i)===1) {
        string += `${sequence}`;
      } else if (number === i && number != 0) {
        string += `+${sequence} = ${count}`;
      } else {
        string += `+${sequence}`;
      }
      sequence++;
    }
    string = string.substring(1);
    return string;
  };
  return SequenceSum;
})();

// didn't allow me to return data this was in kata
// let SequenceSum = function(number) {
//   let sequence = 0;
//   let count = 0;
//
//   for (i=0;i<=number;i++) {
//     count += (i + sequence);
//     sequence++;
//   }
//   return count;
// };






// console.log(SequenceSum.showSequence(6),"0+1+2+3+4+5+6 = 21");
