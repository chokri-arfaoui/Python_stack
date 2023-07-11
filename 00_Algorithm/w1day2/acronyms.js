/* 
  Acronyms

  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 

  Do it with .split first if you need to, then try to do it without
*/

// const str1 = "object oriented programming";
// const expected1 = "OOP";

// // // The 4 pillars of OOP
// // const str2 = "abstraction polymorphism inheritance encapsulation";
// // const expected2 = "APIE";

// // const str3 = "software development life cycle";
// // const expected3 = "SDLC";

// // // Bonus: ignore extra spaces
// // const str4 = "  global   information tracker    ";
// // const expected4 = "GIT";

const str1 = "object oriented programming";
const str1Arr = str1.split(' ');


function acronym(str) {
    varResult = " "

}

// const str = 'Polar Satellite Launch Vehicle';
// const buildAcronym = (str = '') => {
// const strArr = str.split(' ');
// let res = '';
// strArr.forEach(el => {
//     const [char] = el;
//     if(char === char.toUpperCase() && char !== char.toLowerCase()){
//         res += char;
//     };
// });
// return res;
// };
// console.log(buildAcronym(str));