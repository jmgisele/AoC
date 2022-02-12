export { };
const fs = require('fs')

const data = fs.readFileSync('./data.txt', 'utf8')
const result = data.split(/\r?\n/).map((a: string) => {
    const arr = a.split(" ")
    const ans = [arr[0], parseInt(arr[1])]
    return ans;
});
interface Position {
    horizontal: number
    vertical: number
}

//pt 1
const coords: Position = { horizontal: 0, vertical: 0 }

for (let entry of result) {
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
let aim = 0;
const newCoords: Position =  { horizontal: 0, vertical: 0 };

for (let entry of result) {
    switch (entry[0]) {
        case 'forward':
            newCoords.horizontal += entry[1];
            newCoords.vertical += aim * entry[1]
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
