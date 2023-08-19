#!/usr/bin/node
// A function that prints the number of
// arguments already printed and the new argument value. (see example below)
// Prototype: exports.logMe = function (item)
// Output format: <number arguments already printed>: <current argument value>

let funcCall = -1; // Initialize the count to -1 to start from 0
exports.logMe = function (item) {
  funcCall++; // Increment funcCall by 1 on each function call
  console.log(`${funcCall}: ${item}`); // Print the argument and the total count
};

/*
-> My old code  *** Wrong ***
// #!/usr/bin/node
exports.logMe = function (item) {
  let funcCall = 0;

  function incrementFuncCall () {
    funcCall++;
  }

  function getFuncCallCount () {
    return funcCall;
  }

  return {
    incrementFuncCall,
    getFuncCallCount
  };

  // let dan = 0;
  console.log(`${getFuncCallCount()}: ${item}`);
  // dan++;
};
*/
