const axios = require("axios");
const fs = require('fs');

const options = {
  method: 'GET',
  url: 'https://microsoft-translator-text.p.rapidapi.com/languages',
  params: {'api-version': '3.0'},
  headers: {
    'x-rapidapi-host': 'microsoft-translator-text.p.rapidapi.com',
    'x-rapidapi-key': 'd41002b89bmsh40eb3d9beced242p1ff984jsnd0d013cf03cc'
  }
};

axios.request(options).then(function (response) {
	console.log(response.data);
    const jsonData = JSON.stringify(response.data, null, 4)
    fs.writeFile("language.json", jsonData, function(err) {
        if (err) {
            console.log(err);
        }
    });
}).catch(function (error) {
	console.error(error);
});