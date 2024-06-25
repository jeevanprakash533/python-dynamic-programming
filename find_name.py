# import random
# n=int(input())
# board=[[random.randint(1,5)]*n for i in range(n)]
# for i in board:
#     print(i)

wordbank=[['p','b','p','d','e'],
          ['c','r','r','e','i'],
          ['u','j','i','n','r'],
          ['r','q','y','y','t'],
          ['w','q','a','s','a','z']]
word="priya"
n=len(word)
def find(row,col,i,n,path):
    if i == n:
        print("Valid")
        print(path)
        return True 
        # exit()
    if i<0 or i>=n or j<0 or j>=n:
        return False
    if [row,col] not in path:
        path.append([row,col])
        if wordbank[row][col]==word[i]:
            if find(row+1,col,i+1,n,path):
                return True
            if find(row-1,col,i+1,n,path):
                return True
            if find(row,col+1,i+1,n,path):
                return True
            if find(row,col-1,i+1,n,path):
                return True
        path.remove([row,col])

    # else:
    #     return False
path=[]
for i in range(len(wordbank)):
    for j in range(len(wordbank[0])):
        if find(i,j,0,n,path):
            exit()
            break
else:
    print("Invalid")
find(0,0,0,n,path)