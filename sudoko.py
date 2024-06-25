board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
]
def find(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board [i][j]==0:
                return(i,j)
    return None
def isvalid(board,row,col,no):
    for i in range(len(board[0])):
        if board[row][i]==no:
            return False
    for j in range(len(board)):
        if board[j][col]==no:
            return False
    startrow=3*(row//3)
    startcol=3*(col//3)
    for i in range(startrow,startrow+3):
        for j in range(startcol,startcol+3):
            if board[i][j]==no:
                return False
    return True
def play(board):
    empty=find(board)
    if empty==None:
        return True
    i,j=empty
    for no in range(1,10):
        if isvalid(board,i,j,no):
            board[i][j]=no
            if play(board):
                return True
            board[i][j]=0
    return False
s=play(board)
if s==False:
    print("Invalid")
else:
    for i in board:
        print(i)