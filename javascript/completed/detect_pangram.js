//-----------------
// Description:
//-----------------
//
// Algorithm //
//
// function isPangram(string){
//   //1) create array of the alphabet
//   //2) convert input string into array of chars
//   //3) iterate over input
//       //a)) if input char === any letter in alphabet
//             // remove that letter from alphabet
//       //b)) if input char == number or punctuation
//             // Ignore char
//   //4) if alphabet is empty at input iteration's end
//       //a)) return true
//       //b)) else return false
// }
//
//

function isPangram(string) {
  //1) create array of the alphabet
  let alphabet = [
                    "a","b","c","d","e","f","g",
                    "h","i","j","k","l","m","n","o","p",
                    "q","r","s","t","u","v","w","x","y","z"
                  ];
  //2) convert input string into array of chars
  let inputChars = [...string];
  //3) iterate over input
  for (let character of inputChars) {
  // for (i=0;i<=inputChars.length;i++) {
  //   let thisChar = inputChars[i];
    //a)) if input char === any letter in alphabet
    // let thisChar = character.replaceAll(l"[^A-Za-z]+", "").toLowerCase();
    let thisChar = character.replace(/[^A-Za-z0-9_]/g,"").replace(/ /g,'')
    // let thisChar = thisChar;
    if (alphabet.includes(thisChar.toLowerCase())) {
      // remove that letter from alphabet
      let atIndex = alphabet.indexOf(thisChar.toLowerCase());
      alphabet.splice(atIndex, 1);
    }
    //b)) if input char == number or punctuation
          // Ignore char
  }
  //4) if alphabet is empty at input iteration's end
  if (alphabet.length === 0) {
    //a)) return true
    return true;
  } else {
    return false;
    //b)) else return false
  }
}

var string = "The quick brown fox jumps over the lazy dog.";
console.log(isPangram(string), true);
var string = "This is not a pangram.";
console.log(isPangram(string), false);
