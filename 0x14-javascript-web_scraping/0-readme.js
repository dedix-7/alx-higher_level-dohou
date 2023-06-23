#!/usr/bin/node

const files = require('files');
const myFile = process.argv[2];

files.readFile(myFile, 'utf-8', (error, content) => {
	if (error) {
		console.log(error);
	} else {
		console.log(content);
	}
});
