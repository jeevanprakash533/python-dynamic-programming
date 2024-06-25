coins = [8,3,1,2]
amount  = 3
d= [0]*(amount+1)
        # inorder to find the ways d[0]=1
d[0]=1 

for i in coins:
    for j in range(i,amount+1):
        d[j]=d[j]+d[j-i]
        # present count+previous count
        # previous count=amount-coin
# return d[amount]
print(d[amount])