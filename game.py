print("***** Welcome to Connect Four Game made by Md Mejbhah *****")

class Column:
    def __init__(self, r):
        '''each column has r rows'''
        self.col = [0]*r

    def add_disk(self,c):
        '''add disk to this column'''
        found  = False
        for i in range(len(self.col)-1,-1,-1):
            if self.col[i] == 0:
                self.col[i] = c
                found = True
                break
        return found


class Board:    
    def __init__(self, N):
        '''Board for a Connect-N game, the board will have N+2 Col and N+3 Rows'''
        self.num_row = N + 3
        self.num_col = N + 2
        self.cols = [Column(self.num_row) for i in range(self.num_col)]
        self.player = "\u26AA"
        self.n = N
        
        
    def flip_player(self):
        if self.player =="\u26AA":
            self.player = "\u26AB"
        else:
            self.player = "\u26AA"
    
    def display(self):
        '''display the board'''
        for row in range(self.num_row):
            for column in range(self.num_col):
                print(self.cols[column].col[row],end="   ")
            print()
        
    
    def drop_disk(self, c):
        '''drop a disk at column c'''
        return self.cols[c].add_disk(self.player)
        
    def check_connect_n(self,mylist):
        prev = mylist[0]
        count =1
        for i in mylist[1:]:
            if i == prev and i != 0:
                count += 1
            else:
                prev = i
                count = 1
            if count == self.n:
                return True
        return False

    def check_winning_condition(self):
        '''check if there is a winner'''
        for column in self.cols:
            if self.check_connect_n(column.col):
                return True

        for row in range(self.num_row):
            myrow = []
            for column in self.cols:
                myrow.append(column.col[row])
            if self.check_connect_n(myrow):
                return True
        
        for line in range(1, (self.num_col + self.num_row)) : 
            start_col = max(0, line - self.num_row) 
            count = min(line, (self.num_col - start_col), self.num_row)
            diagonal_list = []
            for j in range(0, count) :
                diagonal_list.append(self.cols[start_col + j].col[min(self.num_row, line) - j - 1])
            if self.check_connect_n(diagonal_list):
                return True
        for line in range(1, (self.num_col + self.num_row)) :
            start_col = max(0,line-self.num_row)
            count = min(line,(self.num_col - start_col),self.num_row)
            diagonal_list = []
            for j in range(0,count):
                diagonal_list.append(self.cols[start_col+j].col[max(self.num_row - line +1,1)+j-1])
            if self.check_connect_n(diagonal_list):
                return True
        return False
    
    def all_occupied(self):
        occupied = True
        for column in self.cols:
            for element in column.col:
                if element == 0:
                    occupied = False
        return occupied
        
def checkInteger(n):
    try:
        int(n)
        return True
    except:
        return False            
    
N = 4 
board = Board(N)

while((not board.check_winning_condition()) and (not board.all_occupied())):
    board.display()
    if board.player == "\u26AA":
        player = "White"
    else:
        player = "Black"
    usercol = input(player + " color player, please enter column: ")
    if checkInteger(usercol) and int(usercol)>=0 and int(usercol)< board.num_col:
        valid = board.drop_disk(int(usercol))
        if valid == True:
            if board.check_winning_condition():
                board.display()
                print("Winner is "+player)
                print("*** Thank You For Playing This Game***")
                break
            board.flip_player()
        else:
            print("Sorry, the column is completely filled")
    else:
        print("please enter a valid column number")
        
        
    
