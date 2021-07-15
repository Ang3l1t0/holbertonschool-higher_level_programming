#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
request(url + id, function (error, response, body) {
  error && console.log(error); // Print the error if one occurred
  console.log(JSON.parse(body).title);
});
