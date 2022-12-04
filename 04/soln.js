"use strict";
exports.__esModule = true;
var fs = require('fs');
var Board = /** @class */ (function () {
    function Board(gameBoard) {
        this.hasWon = false;
        this.gameBoard = gameBoard;
        this.winningNumsBoard = this.constructWinningNumsBoard();
        this.winningNum = undefined;
        this.rows = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0 };
        this.cols = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0 };
    }
    Board.prototype.constructWinningNumsBoard = function () {
        var dict = {};
        for (var i = 0; i < this.gameBoard.length; i++) {
            for (var j = 0; j < this.gameBoard[0].length; j++) {
                dict["r" + i + "c" + j] = [this.gameBoard[i][j], false];
            }
        }
        return dict;
    };
    Board.prototype.markNum = function (num) {
        for (var i = 0; i < this.gameBoard.length; i++) {
            for (var j = 0; j < this.gameBoard[0].length; j++) {
                if (this.gameBoard[i][j] === num) {
                    this.winningNumsBoard["r" + i + "c" + j][1] = true;
                    this.rows[i]++;
                    this.cols[j]++;
                }
            }
        }
        if (this.checkWon()) {
            this.hasWon = true;
            this.winningNum = num;
            return true;
        }
        return false;
    };
    Board.prototype.checkWon = function () {
        if (Object.values(this.rows).includes(5))
            return true;
        if (Object.values(this.cols).includes(5))
            return true;
        return false;
    };
    return Board;
}());
var Game = /** @class */ (function () {
    function Game() {
        this.boards = this.constructBoards();
        this.winningNums = this.constructNums();
    }
    Game.prototype.constructBoards = function () {
        var data = fs.readFileSync('./boards.txt', 'utf8');
        var rawBoards = data.split(/\r?\n/);
        var dictBoards = {};
        var currBoard = [];
        for (var i = 0; i < rawBoards.length; i++) {
            //this is just massaging data into useable format
            var line = rawBoards[i];
            if (line === '') {
                dictBoards[i] = new Board(currBoard);
                currBoard = [];
                continue;
            }
            var l = line.split(' ');
            var arr = l.filter(function (str) { return str !== ''; }).map(function (str) { return parseInt(str); });
            currBoard.push(arr);
            if (i === rawBoards.length - 1)
                dictBoards[i] = new Board(currBoard);
        }
        return dictBoards;
    };
    Game.prototype.constructNums = function () {
        var numData = fs.readFileSync('./nums.txt', 'utf8');
        var numbersArray = numData.split(',').map(function (str) { return parseInt(str); });
        return numbersArray;
    };
    Game.prototype.playUntilOneWon = function () {
        var i = 0;
        while (true) {
            for (var board in this.boards) {
                var currBoard = this.boards[board];
                var currNum = this.winningNums[i];
                var roundWon = currBoard.markNum(currNum);
                if (roundWon)
                    return this.calcScore(currBoard.winningNumsBoard, currNum);
            }
            i++;
        }
    };
    Game.prototype.playUntilAllWon = function () {
        var i = 0;
        var numBoards = Object.keys(this.boards).length;
        var numWon = 0;
        var lastWon = undefined;
        while (numWon < numBoards) {
            for (var board in this.boards) {
                if (!this.boards[board].hasWon) {
                    var roundWon = this.boards[board].markNum(this.winningNums[i]);
                    if (roundWon) {
                        numWon++;
                        lastWon = this.boards[board];
                    }
                }
            }
            i++;
        }
        return this.calcScore(lastWon.winningNumsBoard, lastWon.winningNum);
    };
    Game.prototype.calcScore = function (winningNumsBoard, winningNum) {
        var total = 0;
        for (var entry in winningNumsBoard) {
            total += winningNumsBoard[entry][1] === false ? winningNumsBoard[entry][0] : 0;
        }
        return total * winningNum;
    };
    return Game;
}());
var PlayGame = new Game();
console.log(PlayGame.playUntilOneWon());
console.log('new game');
var LoseGame = new Game();
console.log(LoseGame.playUntilAllWon());
