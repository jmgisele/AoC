"use strict";
exports.__esModule = true;
var fs = require('fs');
var data = fs.readFileSync('./data.txt', 'utf8');
var result = data.split(/\r?\n/).map(function (a) {
    var arr = a.split(" ");
    var ans = [arr[0], parseInt(arr[1])];
    return ans;
});
//pt 1
var coords = { horizontal: 0, vertical: 0 };
for (var _i = 0, result_1 = result; _i < result_1.length; _i++) {
    var entry = result_1[_i];
    switch (entry[0]) {
        case 'forward':
            coords.horizontal += entry[1];
            break;
        case 'down':
            coords.vertical += entry[1];
            break;
        case 'up':
            coords.vertical -= entry[1];
            break;
    }
}
console.log(coords.horizontal * coords.vertical);
//pt 2
var aim = 0;
var newCoords = { horizontal: 0, vertical: 0 };
for (var _a = 0, result_2 = result; _a < result_2.length; _a++) {
    var entry = result_2[_a];
    switch (entry[0]) {
        case 'forward':
            newCoords.horizontal += entry[1];
            newCoords.vertical += aim * entry[1];
            break;
        case 'down':
            aim += entry[1];
            break;
        case 'up':
            aim -= entry[1];
            break;
    }
}
console.log(newCoords.horizontal * newCoords.vertical);
