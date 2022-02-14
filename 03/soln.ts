export { };
const fs = require('fs')

const data = fs.readFileSync('./data.txt', 'utf8')
const result = data.split(/\r?\n/);


//pt 1
const powerConsumption = (arr: string[]) => {
    let gamma = ''
    for (let i = 0; i < arr[0].length; i++) {
        let total = 0;
        for (let j = 0; j < arr.length; j++) {
            total += parseInt(arr[j][i])
        }
        total = total / arr.length;
        total = total >= 0.5 ? 1 : 0;
        gamma += total.toString();
    }
    let eps = ''
    for (let i = 0; i < gamma.length; i++) {
        switch (gamma[i]) {
            case '1':
                eps += '0';
                break;
            case '0':
                eps += '1';
                break;
        }
    }
    return [gamma, eps]
}

//just convert these & multiply for pt 1
console.log(powerConsumption(result));

//pt 2
let [gamm, eps] = powerConsumption(result);

function oxygenGenerator(arr: string[], index: number = 0): string | Function {
    let avg = 0;
    for (let j = 0; j < arr.length; j++) {
        avg += parseInt(arr[j][index])
    }
    avg = avg / arr.length;
    const strToCompare = avg >= 0.5 ? '1' : '0';
    const oxArr = arr.filter(entry => entry[index] === strToCompare);
    if (oxArr.length === 1) return oxArr[0].toString();
    return oxygenGenerator(oxArr, index + 1)
}

// can't iterate over both at once without conditions
// because they might have different base cases
//easier to just re-run
function co2Generator(arr: string[], index: number = 0): string | Function {
    let avg = 0;
    for (let j = 0; j < arr.length; j++) {
        avg += parseInt(arr[j][index])
    }
    avg = avg / arr.length;
    const strToCompare = avg >= 0.5 ? '0' : '1';
    const co2Arr = arr.filter(entry => entry[index] === strToCompare);
    if (co2Arr.length === 1) return co2Arr[0].toString();
    return co2Generator(co2Arr, index + 1)
}

// convert and multiply for pt 2
console.log(oxygenGenerator(result));
console.log(co2Generator(result));