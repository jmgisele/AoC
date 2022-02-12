var fs = require('fs');
var data = fs.readFileSync('./input.txt', 'utf8');
var result = data.split(/\r?\n/).map(function (a) { return parseInt(a); });
// part one
var greaterThan = function (input) {
    var answer = 0;
    for (var i = 0; i < input.length - 1; i++) {
        if (input[i] < input[i + 1])
            answer++;
    }
    return answer;
};
console.log(greaterThan(result));
//part two
var combinedResult = [];
for (var i = 1; i < result.length - 1; i++) {
    combinedResult.push(result[i - 1] + result[i] + result[i + 1]);
}
console.log(greaterThan(combinedResult));
