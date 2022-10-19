#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const myURL = `${myArgs[0]}`;
let key = 'characters';

// request(myURL, function (error, response, body) {
//   if (error) {
//     console.log(error);
//   } else {
//     const res = JSON.parse(body).results;
//     for (let i = 0; i <= res.length; i++) {
//       for (key in res[i]) {
//         if (key === 'characters') {
//           for (let j = 0; j < res[i].characters.length; j++) {
//             var count = 0;
//             while (res[i].characters[j] == 'https://swapi-api.hbtn.io/api/people/18/') {
//               // console.log('found');
//               j++;
//               count += 1;
//             }
//           }
//         }
//       }
//     }
//     console.log('count: ', count);
//   }
// });

ch_url = 'https://swapi-api.hbtn.io/api/people/18/'

request(ch_url, function (error, response, body) {
      if (error) {
        console.log(error);
      } else {
        const res = JSON.parse(body)
        console.log(res.films.length)
      }
});
