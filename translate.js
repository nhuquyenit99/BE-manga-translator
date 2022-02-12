#! /usr/bin/env node
const translate = require('@vitalets/google-translate-api');

translate(process.argv[2], {from: 'ja', to: 'en'}).then(res => {
    console.log(res.text);
}).catch(err => {
    console.error(err);
});

// let qs = require("qs")
// let axios = require("axios")

// const options = {
//     method: "POST",
//     url: "https://google-translate1.p.rapidapi.com/language/translate/v2",
//     data: qs.stringify({
//         q : process.argv[2],
//         source : "ja",
//         target : "en"
//     }),
//     headers: {
//         "content-type": "application/x-www-form-urlencoded",
//         "accept-encoding": "application/gzip",
//         "x-rapidapi-key": "d41002b89bmsh40eb3d9beced242p1ff984jsnd0d013cf03cc",
//         "x-rapidapi-host": "google-translate1.p.rapidapi.com"
//     }
// };

// axios.request(options)
//     .then(function (response) {
//         console.log(response.data.data["translations"][0]["translatedText"]);
//     }).catch(function (error) {
//     console.error(error);
// });

// const translate = require('translate-google')

// translate(JSON.parse(process.argv[2]), {to: 'en'}).then(res => {
//     console.log(res)
// }).catch(err => {
//     console.error(err)
// })

