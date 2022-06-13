// Calculate BMI
// 
// 8 kyu
// 
// Write function bmi that calculates body mass index (bmi = weight / height2).
// if bmi <= 18.5 return "Underweight"
// if bmi <= 25.0 return "Normal"
// if bmi <= 30.0 return "Overweight"
// if bmi > 30 return "Obese"

const bmi = (weight, height) => {
  const result = weight / (height ** 2);
  if (result <= 18.5) {
    return "Underweight"
  }
  if (result <= 25) {
    return "Normal"
  }
  if (result <= 30) {
    return "Overweight"
  }
  if ( result > 30) {
    return "Obese"
  }
};

//
// Tests
//
console.log(bmi(80, 1.80), "Normal")
