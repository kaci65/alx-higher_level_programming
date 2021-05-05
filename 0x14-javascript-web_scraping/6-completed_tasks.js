#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');
if (process.argv.length === 3) {
  const url = process.argv[2];
  request(url, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      const numTasks = {};
      const tasksList = JSON.parse(body);
      for (let i = 0; i < tasksList.length; i++) {
        if (tasksList[i].completed === true) {
          if (numTasks[tasksList[i].userId] === undefined) {
            numTasks[tasksList[i].userId] = 1;
          } else {
            numTasks[tasksList[i].userId]++;
          }
        }
      }
      console.log(numTasks);
    }
  });
}
