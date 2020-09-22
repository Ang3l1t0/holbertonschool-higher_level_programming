#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  !error && console.log(JSON.parse(body).reduce(function (total, current) {
    current.completed && (total[current.userId] = (total[current.userId] || 0) + 1);
    return total;
  }, {}));
});
