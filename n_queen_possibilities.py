# n=int(input("Queens? "))
# board=[[0]*n for i in range(n)]
# for i in board:
#     print(i)
def issafe(board,i,j,n):
    orgi=i #if we dont assign original values down diagonal is not possible while checking by this line i an j values doesnt change
    orgj=j
    # for col in range(j):
    for col in range(n):
        if board[i][col]=="q":
            return False
    # for row in range(i):
    for row in range(n):
        if board[row][j]=="q":
            return False
    while i>=0 and i<n and j>=0 and j<n:
        if board[i][j]=="q":
            return False
        i-=1
        j-=1
    i=orgi
    j=orgj
    while i>=0 and i<n and j>=0 and j<n:
        if board[i][j]=="q":
            return False
        i-=1
        j+=1
    return True            
def play(board,row,col,n):
    if row==n:
        for i in board:
            print(i)
        exit()
    for i in range(col):
        if issafe(board,row,i,n):
            # back tracking 
            board[row][i]="q"
            play(board,row+1,col,n)
            board[row][i]=0
n=int(input("Queens? "))
board=[[0]*n for i in range(n)]
play(board,0,n,n)
