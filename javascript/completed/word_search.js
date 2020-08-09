//-----------------
// Description: Wordsearch
//-----------------
//
// Given an array called text and a word named likewise
// Is the given word contained in the text array?
// function wordSearch(word, text){
      // input here..
// }
//
// const myText = "what makes the desert beautiful, said the little prince is that somewhere it hides a well";
//
// Test.describe("Fixed Tests (new)", _ => {
//   Test.it("Tests", __ => {
//     Test.assertEquals(wordSearch("desert",myText),true);
//     Test.assertEquals(wordSearch("blue",myText),false);
//     Test.assertEquals(wordSearch("well",myText),true);
//     Test.assertEquals(wordSearch("house",myText),false);
//     Test.assertEquals(wordSearch("beautiful",myText),true);
//     Test.assertEquals(wordSearch("prince",myText),true);
//     Test.assertEquals(wordSearch("le prince",myText),false);
//   });
// });
var myText = "what makes the desert beautiful, said the little prince is that somewhere it hides a well";
let text = "what makes the desert beautiful, said the little prince is that somewhere it hides a well";
function wordSearch(word, myText) {
  var regex = /,/;
  var array = myText.split(' ');
  for (i=0;i<=myText.length;i++) {
    if (array[i] ===',') {
      array.splice(myText[i], 1);
    }
  }
  let joinedText = array.join(' ');
  var splitText = joinedText.split(' ');
  let payload = Object.values(splitText);
  return payload.includes(word);
}

console.log(wordSearch("desert", myText));

console.log(wordSearch("desert",myText),true);
console.log(wordSearch("blue",myText),false);
console.log(wordSearch("well",myText),true);
console.log(wordSearch("house",myText),false);
console.log(wordSearch("beautiful",myText),true);
console.log(wordSearch("prince",myText),true);
console.log(wordSearch("le prince",myText),false);
