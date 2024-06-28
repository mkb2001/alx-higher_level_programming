#!/usr/bin/node
const args = process.argv.slice(2);

const firstArg = args[0] !== undefined ? args[0] : "";
const secondArg = args[1] !== undefined ? args[1] : "";

console.log(`${firstArg} is ${secondArg}`);
