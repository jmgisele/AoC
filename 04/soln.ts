export { };
const fs = require('fs')

interface WonDict {
    [rowcol: string]: [number, boolean]
}

class Board {
    hasWon: boolean;
    gameBoard: number[][];
    winningNumsBoard: WonDict;
    winningNum: number | undefined;
    rows: { [index: number]: number }
    cols: { [index: number]: number }

    constructor(gameBoard: number[][]) {
        this.hasWon = false;
        this.gameBoard = gameBoard;
        this.winningNumsBoard = this.constructWinningNumsBoard();
        this.winningNum = undefined;
        this.rows = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0 }
        this.cols = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0 }
    }

    constructWinningNumsBoard() {
        const dict: WonDict = {};
        for (let i = 0; i < this.gameBoard.length; i++) {
            for (let j = 0; j < this.gameBoard[0].length; j++) {
                dict[`r${i}c${j}`] = [this.gameBoard[i][j], false];
            }
        }
        return dict;
    }

    markNum(num: number) { //returns true if it's won
        for (let i = 0; i < this.gameBoard.length; i++) {
            for (let j = 0; j < this.gameBoard[0].length; j++) {
                if (this.gameBoard[i][j] === num) {
                    this.winningNumsBoard[`r${i}c${j}`][1] = true;
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
    }

    checkWon() {
        if (Object.values(this.rows).includes(5)) return true;
        if (Object.values(this.cols).includes(5)) return true;
        return false;
    }
}


//setting up game

//setting up numbers

interface DictBoards {
    [index: number]: Board
}

class Game {
    boards: DictBoards;
    winningNums: number[];

    constructor() {
        this.boards = this.constructBoards();
        this.winningNums = this.constructNums();
    }

    constructBoards() {
        const data = fs.readFileSync('./boards.txt', 'utf8')
        const rawBoards = data.split(/\r?\n/);

        const dictBoards: DictBoards = {};
        let currBoard: number[][] = [];
        for (let i = 0; i < rawBoards.length; i++) {
            //this is just massaging data into useable format
            let line = rawBoards[i];
            if (line === '') {
                dictBoards[i] = new Board(currBoard);
                currBoard = [];
                continue;
            }
            let l = line.split(' ');
            let arr = l.filter((str: string) => str !== '').map((str: string) => parseInt(str));
            currBoard.push(arr)
            if (i === rawBoards.length - 1) dictBoards[i] = new Board(currBoard);
        }
        return dictBoards;
    }

    constructNums() {
        const numData = fs.readFileSync('./nums.txt', 'utf8');
        const numbersArray = numData.split(',').map((str: string) => parseInt(str));
        return numbersArray;
    }

    playUntilOneWon(): number {
        let i = 0;
        while (true) {
            for (let board in this.boards) {
                let currBoard = this.boards[board];
                let currNum = this.winningNums[i];
                let roundWon = currBoard.markNum(currNum);
                if (roundWon) return this.calcScore(currBoard.winningNumsBoard, currNum);
            }
            i++;
        }
    }

    playUntilAllWon(): number {
        let i = 0;
        let numBoards = Object.keys(this.boards).length;
        let numWon = 0;
        let lastWon: Board | undefined = undefined;
        while (numWon < numBoards) {
            for (let board in this.boards) {
                if (!this.boards[board].hasWon) {
                    let roundWon = this.boards[board].markNum(this.winningNums[i]);
                    if (roundWon) {
                        numWon++;
                        lastWon = this.boards[board];
                    }
                }
            }
            i++;
        }
        return this.calcScore(lastWon!.winningNumsBoard, lastWon!.winningNum!);
    }

    calcScore(winningNumsBoard: WonDict, winningNum: number) {
        let total = 0;
        for (let entry in winningNumsBoard) {
            total += winningNumsBoard[entry][1] === false ? winningNumsBoard[entry][0] : 0;
        }
        return total * winningNum;
    }
}

const PlayGame = new Game()
console.log(PlayGame.playUntilOneWon());

console.log('new game')
const LoseGame = new Game()
console.log(LoseGame.playUntilAllWon());