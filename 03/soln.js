"use strict";
exports.__esModule = true;
var fs = require('fs');
var data = fs.readFileSync('./data.txt', 'utf8');
var result = data.split(/\r?\n/);
//pt 1
var powerConsumption = function (arr) {
    var gamma = '';
    for (var i = 0; i < arr[0].length; i++) {
        var total = 0;
        for (var j = 0; j < arr.length; j++) {
            total += parseInt(arr[j][i]);
        }
        total = total / arr.length;
        total = total >= 0.5 ? 1 : 0;
        gamma += total.toString();
    }
    var eps = '';
    for (var i = 0; i < gamma.length; i++) {
        switch (gamma[i]) {
            case '1':
                eps += '0';
                break;
            case '0':
                eps += '1';
                break;
        }
    }
    return [gamma, eps];
};
//just convert these & multiply for pt 1
console.log(powerConsumption(result));
//pt 2
var _a = powerConsumption(result), gamm = _a[0], eps = _a[1];
function oxygenGenerator(arr, index) {
    if (index === void 0) { index = 0; }
    var avg = 0;
    for (var j = 0; j < arr.length; j++) {
        avg += parseInt(arr[j][index]);
    }
    avg = avg / arr.length;
    var strToCompare = avg >= 0.5 ? '1' : '0';
    var oxArr = arr.filter(function (entry) { return entry[index] === strToCompare; });
    if (oxArr.length === 1)
        return oxArr[0].toString();
    return oxygenGenerator(oxArr, index + 1);
}
console.log(oxygenGenerator(result));
// can't iterate over both at once without conditions
// because they might have different base cases
//easier to just re-run
function co2Generator(arr, index) {
    if (index === void 0) { index = 0; }
    var avg = 0;
    for (var j = 0; j < arr.length; j++) {
        avg += parseInt(arr[j][index]);
    }
    avg = avg / arr.length;
    var strToCompare = avg >= 0.5 ? '0' : '1';
    var co2Arr = arr.filter(function (entry) { return entry[index] === strToCompare; });
    if (co2Arr.length === 1)
        return co2Arr[0].toString();
    return co2Generator(co2Arr, index + 1);
}
console.log(co2Generator(result));
