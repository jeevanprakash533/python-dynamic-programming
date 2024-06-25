# horse in chess
import sys
sys.setrecursionlimit(10000)     #default recurrsion limit is 1000
kmoves=[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]


n=8
def issafe(r,c,board):
    return 0<=r<8 and 0<=c<8 and board[r][c]==-1
board=[[-1]*n for i in range(n)]
# for i in board:
#     print(i)   these lines print the board in form of list
def play(board,row,col,n,move):
    if move==n*n:
        for i in board:
            print(i)
        return True
    for m in kmoves:
        a,b=m
        nrow=row+a
        ncol=col+b
        if issafe(nrow,ncol,board):
            board[nrow][ncol]=move
            if play(board,nrow,ncol,n,move+1):
                return True
            board[row][col]=-1
    return False
board[0][0]=0
play(board,0,0,n,1)


