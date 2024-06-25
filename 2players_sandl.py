# snake:ladder two players
import random
sandl={24:5,38:12,47:23,70:36,80:55,98:58,57:27,34:19,45:14,76:4}
def movedice(playerpos,dice):
    newposition=playerpos+dice
    print("before position is ",newposition)
    if newposition in sandl:
        newposition=sandl[newposition]
        print("You are bitten by a snake")
        return newposition
    elif newposition in sandl.values():
        for i in sandl:
            if sandl[i]==newposition:
                newposition=i
                break
        print("You found a ladder")
        return newposition
    else:
        return newposition
def printboard(playerpos1,playerpos2):
    for row in range(10,0,-1):
        for col in range(1,11):
            newno=(row)*10-col
            if newno==playerpos1:
                print("[p1]",end=" ")
            elif newno==playerpos2:
                print("[p2]",end=" ")
            elif newno in sandl:
                print("[s]",end=" ")
            else:
                print("[-]",end=" ")
        print()
def diceroll():
    return random.randint(1,6)
print("Welcome to Snake and Ladder Game")
print ("-"*50)
playerpos1=0
playerpos2=0
curr=playerpos1
flag=0
while playerpos1<100 and playerpos2<100:
    if flag==0:
        print("player is player1")
        print("Player position at ",curr)
        input("Press Enter to start")
        dice=diceroll()
        print("Your number is ",dice)
        move=movedice(playerpos1,dice)
        print("Your new position is ",move)
        playerpos1=move
        print()
        printboard(playerpos1,playerpos2)
        print()
        print("*"*50)
        flag=1
    else:
        print("player is player2") 
        print("Player position at ",curr)
        input("Press Enter to start")
        dice=diceroll()
        print("Your number is ",dice)
        move=movedice(playerpos2,dice)
        print("Your new position is ",move)
        playerpos2=move
        print()
        printboard(playerpos2,playerpos1)
        print()
        print("*"*50)
        flag=0
if playerpos1>=100:
        print("Player1 won")
elif playerpos2>=100:
        print("Player 2 won")