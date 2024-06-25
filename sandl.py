# snake:ladder one player
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
def printboard(playerpos):
    for row in range(10,0,-1):
        for col in range(1,11):
            newno=(row)*10-col
            if newno==playerpos:
                print("[p]",end=" ")
            elif newno in sandl:
                print("[s]",end=" ")
            else:
                print("[-]",end=" ")
        print()
def diceroll():
    return random.randint(1,6)
print("Welcome to Snake and Ladder Game")
print ("-"*50)
playerpos=0
while playerpos<100:
    print("Player position at ",playerpos)
    input("Press Enter to start")
    dice=diceroll()
    print("Your number is ",dice)
    move=movedice(playerpos,dice)
    print("Your new position is ",move)
    playerpos=move
    print()
    printboard(playerpos)
    print()
    print("*"*50)
print("You Won the Game")


