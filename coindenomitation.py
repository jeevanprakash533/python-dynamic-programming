coins = [1,2,5,10]
amount  = 10
memo = [0]*(amount+1)
for i in coins:
    for a in range(i,amount+1):
        memo[a] = memo[a-i]+1
# prints the indexes of the amount
print(memo) 
# prints the min coins required
print(memo[amount])
