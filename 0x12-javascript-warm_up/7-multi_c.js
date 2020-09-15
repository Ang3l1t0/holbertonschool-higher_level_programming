#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  if (parseInt(process.argv[2])) {
    const num = parseInt(process.argv[2]);
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  }
}
