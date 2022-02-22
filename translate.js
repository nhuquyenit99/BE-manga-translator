#! /usr/bin/env node
const translate = require('@vitalets/google-translate-api');

translate(process.argv[2], {from: 'ja', to: process.argv[3]}).then(res => {
    console.log(res.text);
}).catch(err => {
    console.error(err);
});

/*
MICROSOFT TRANSLATE API -> translate better
*/
// const axios = require("axios")

// var options = {
//     method: 'POST',
//     url: 'https://microsoft-translator-text.p.rapidapi.com/translate',
//     params: {
//         to: process.argv[3],
//         'api-version': '3.0',
//         from: 'ja',
//         profanityAction: 'NoAction',
//         textType: 'plain'
//     },
//     headers: {
//         'content-type': 'application/json',
//         'x-rapidapi-host': 'microsoft-translator-text.p.rapidapi.com',
//         'x-rapidapi-key': 'd41002b89bmsh40eb3d9beced242p1ff984jsnd0d013cf03cc'
//     },
//     data: [{Text: process.argv[2]}]
// };

// axios.request(options).then(function (response) {
//     console.log(response.data?.[0]?.translations?.[0].text);
// }).catch(function (error) {
//     console.error(error);
// });

