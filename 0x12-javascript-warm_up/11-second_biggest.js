#!/usr/bin/node

function secondMax() {
    let max = -Infinity;
    let secondMax = -Infinity;
    for (let i = 0; i < arguments.length; i++) {
        let num = parseInt(arguments[i]);
        if (num > max) {
            secondMax = max;
            max = num;
        } else if (num > secondMax && num < max) {
            secondMax = num;
        }
    }
    console.log(secondMax === -Infinity ? 0 : secondMax);
}
