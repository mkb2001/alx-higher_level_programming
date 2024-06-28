#!/usr/bin/node

const args = process.argv.slice(2);
const num = Number.parseInt(args[0], 10);

function factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

if (Number.isNaN(num)) {
    console.log(factorial(1));  // Factorial of NaN is treated as factorial of 1
} else {
    console.log(factorial(num));
}
