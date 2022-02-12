export {};
const fs = require('fs')

const data = fs.readFileSync('./input.txt', 'utf8')
const result = data.split(/\r?\n/).map((a: string) => parseInt(a));


// part one
const greaterThan = (input: number[]) => {
    let answer = 0;
    for (let i = 0; i < input.length - 1; i++) {
        if (input[i] < input[i + 1]) answer++;
    }
    return answer
}
console.log(greaterThan(result))

//part two
let combinedResult: number[] = []
for (let i = 1; i < result.length - 1; i++) {
    combinedResult.push(result[i - 1] + result[i] + result[i + 1])
}
console.log(greaterThan(combinedResult))