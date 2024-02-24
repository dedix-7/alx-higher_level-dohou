#!/usr/bin/node
/**
 * The fs module provides file system-related functions, such as reading and writing files
 * The fs module enables interacting with the file system in a way modeled on standard POSIX functions.
 *
 * The algorithm here is simple:
 * First, read the files entered as command line arguments using fs.readFileSync()
 * The fs.readFileSync() is a synchronous function that reads the contents of a file synchronously,
 * meaning that it blocks the execution of the program until the file is read.
 * It takes two arguments: the file path and the encoding (optional).
 * It returns the data read from the file directly as a string or a Buffer (depending on the encoding used).
 * Now, the utf-8 argument specifies the encoding of the file, which is set to 'utf-8' to read the file as text.
 * Now that the files are being read by the fs.readFileSync(), and are being stored into two variables, you can then
 * concatenate the contents of the two files into a variable using string concatenation of the first two variables.
 * Then, we can write the contents of this variable to the command line from our third variable, into another variable
 * using an fs method that works just the same way the fs.readFileSync() function works: the fs.writeFileSync().
 * Remember to specify the encoding as 'utf-8', set to, this time, write the variable value as text into our final new file.
 */
const fs = require('fs');
const firstFile = fs.readFileSync(process.argv[2], 'utf-8');
const secondFile = fs.readFileSync(process.argv[3], 'utf-8');
const concatenatedFile = firstFile + secondFile;
fs.writeFileSync(process.argv[4], concatenatedFile, 'utf-8');
