import numpy as np
with open('nums.txt', 'r') as data:
    nums = list(map(lambda n: int(n), data.read().split(",")))


with open('boards.txt', 'r') as data:
    board_list = data.read().splitlines()

#pt 1

class Board(object):
    def __init__(self, n, list):
        self.n = n
        self.list = list
        self.make_board()
        self.make_dict()
        self.hasWon = False
        self.rows()
        self.cols()

    def __str__(self):
        return str(self.list)

    def make_board(self):
        ''' Takes list and turns into numpy array board,
        sets self.board to that board
        '''
        self.board = np.array(self.list) 

    def make_dict(self):
        ''' Takes a numpy array and 
        sets self.dict to a dictionary with 'i,j' representing the 
        [m,n] place in the board. Sets all dict values to [number, False].
        '''
        dict = {}
        for i in range(0,5):
            for j in range(0,5):
                dict["{},{}".format(i,j)] = [int(self.board[i,j]), False]

        self.dict = dict

    def rows(self):
        self.rows = {"row0" : 0, "row1": 0, "row2": 0, "row3":0, "row4": 0}

    def cols(self):
        self.cols = {"col0" : 0, "col1": 0, "col2": 0, "col3":0, "col4": 0}

    def BINGO(self, number_called):
        ''' Takes a single board and calls a number on it
        If the board doesn't win, updates self.rows and self.cols;
        if the board wins, also sets hasWon to True
        '''
        for location, value in self.dict.items():
            if value[0] == number_called:
                loc = str(location)
                if (value[1] == False):
                    self.rows["row{}".format(loc[0])] += 1
                    self.cols["col{}".format(loc[2])] += 1
                    self.dict[location] = [value[0],True]
        for i in range(0,5):
            if self.rows["row{}".format(i)] == 5 or self.cols["col{}".format(i)] == 5:
                self.hasWon = True

class Game(object):
    def __init__(self,nums,arr):
        self.nums = nums
        self.originalarr = arr
        self.game_over = False
        self.splitIntoBoards()
        self.play_bingo()
        self.play_failing_bingo()

    def splitIntoBoards(self):
        '''Takes original list and 
        splits into Board objects. 
        Sets dict to self.boards_dict'''
        boards_dict = {}
        board_num = 0
        n = 0
        while (n < len(self.originalarr)):
            this_board = []
            for i in range (0,5):
                this_row = list(filter(None, self.originalarr[n+i].split(" ")))
                this_board.append(this_row)
            boards_dict[board_num] = Board(board_num,this_board)# push to boards_dict
            n += 6 #skipping the ''
            board_num += 1 #keeping track of board n
        self.boards_dict = boards_dict
    
    def calcFinal(self):
        winning_dict = self.winning_board.dict
        sum = 0
        for value in winning_dict.values():
            if value[1] == False:
                sum += value[0]
        return sum * self.winning_number

    def reset_boards(self):
        for board in self.boards_dict.values():
            board.hasWon = False

    #pt 1    
    def play_bingo(self):
        ''' Runs BINGO on each board until one wins'''
        i = 0
        while self.game_over == False:
            for board in self.boards_dict.values():
                board.BINGO(self.nums[i])
                if board.hasWon == True:
                    self.winning_board = board
                    self.winning_number = self.nums[i]
                    self.game_over = True
                    self.answer1 = self.calcFinal()
            i += 1
        self.reset_boards()


    #pt 2
    def play_failing_bingo(self):
        ''' Runs BINGO on each board, keeping 
        track of final board to win '''
        i = 0
        num_winning_boards = 0
        while i < len(self.nums):
            for board in self.boards_dict.values():
                if board.hasWon == True:
                    continue #we've already counted it
                else:
                    board.BINGO(self.nums[i])
                    if board.hasWon == True:
                        self.winning_board = board
                        self.winning_number = self.nums[i]
                        num_winning_boards += 1
                        if num_winning_boards >= len(self.boards_dict.values()):
                            self.answer2 = self.calcFinal()
            i += 1
        self.reset_boards()



game = Game(nums, board_list)

print(game.answer1,game.answer2)

