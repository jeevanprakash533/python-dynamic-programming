
def printboard(board):
    # print("*"*20)
    print("-"*15)
    for row in board:
        print("     |".join(row))
        print("-"*15)
    # print("*"*20)
def isfull(board):
    for row in board:
        for col in row:
            if col=="":
                return False
    else:
        return True
def check(board,p):
    for row in board:
        if row[0]==p and row[1]==p and row[2]==p:
            return True
    for i in range(3):
        if board[0][i]==p and board[1][i]==p and board[2][i]==p:
            return True
    if board[1][1]==p and board[2][2]==p and board[0][0]==p:
        return True
    if board[0][2]==p and board[1][1]==p and board[2][0]==p:
        return True 
board=[[""]*3 for i in range(3)]     
print("welcome to game,tic tac toe")
printboard(board)
print("Player - X and 0")
currentplayer='X'
while True:
    print("Current player is ",currentplayer)
    print("Enter the Dimension")
    X,Y=map(int,input().split())

    if -1<X<3 and -1<Y<3:
      if board[X][Y]=="":
        board[X][Y]=currentplayer
        printboard(board)
        if check(board,currentplayer):
            print("Congratulations",currentplayer,"Wins")
            break
        if isfull(board):
            print("Game is draw")
            break
        if currentplayer=="X":
                currentplayer="0"
        else:
                currentplayer="X"
    else:
            print("Enter a valid number")
        
