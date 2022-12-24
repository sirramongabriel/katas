// School Paperwork
//
// 8 kyu
// 
// Your classmates asked you to copy some paperwork for them. 
// You know that there are 'n' classmates and the paperwork has 'm' pages.

// Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

//
// Example:
//
// n= 5, m=5: 25
// n=-5, m=5:  0 

const paperwork = (classmates, pages) => {
  if (classmates < 0 || pages < 0) {
    return 0;
  }
  return classmates * pages;
};

//
// Tests
//
console.log(paperwork(5,5), 25, 'Should be 25');
console.log(paperwork(5,-5), 0, 'Should be 0');
console.log(paperwork(-5,-5), 0, 'Should be 0');
console.log(paperwork(-5,5), 0, 'Should be 0');
console.log(paperwork(5,0), 0, 'Should be 0');