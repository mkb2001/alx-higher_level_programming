#!/usr/bin/node

const args = process.argv.slice(2);
const a = Number.parseInt(args[0], 10);
const b = Number.parseInt(args[1], 10);

function add(a, b) {
    return a + b;
}

if (Number.isNaN(a) || Number.isNaN(b)) {
    console.log("Invalid input");
} else {
    console.log(add(a, b));
}
